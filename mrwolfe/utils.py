import re
import mimetypes
import chardet
from html2text import html2text
from tnefparse.tnef import TNEF
from django.conf import settings
from django.core.files.base import ContentFile
from mrwolfe.models.attachment import Attachment
from mrwolfe.models.contact import Contact
from mrwolfe.models.sla import SLA
from mrwolfe.models.issue import Issue
from notification import notify


ISSUE_SUBJECT_MATCH = re.compile('#([0-9]{8})')


def determine_sla(message):

    """ Determine to what SLA this email message is addressed. Return None
    if this cannot be determined. The email_message is a parsed message
    as per email.parser """

    for sla in SLA.objects.all():
        for rule in sla.rule_set.all():
            if rule.matches(message):
                return sla

    return None


def handle_message(message):

    sla = determine_sla(message)
    sender = None

    from_addr = message['from']
    send_from = settings.DEFAULT_FROM_ADDR

    if re.search('<[^>]*>', from_addr):
        from_addr = re.search('<([^>]*)>', from_addr).groups(0)[0]

    if not Contact.objects.filter(email=from_addr).exists():
        if settings.ALLOW_NON_CONTACTS:
            sender = Contact.objects.create(email=from_addr)
        else:
            notify("issue_bounced", {}, send_from, from_addr)
            return False
    else:
        sender = Contact.objects.filter(email=from_addr)[0]

    if sla and not sla.is_contact(sender) and not \
            settings.ALLOW_NON_CONTACTS:
        notify("issue_bounced", {}, send_from, from_addr)
        return False

    # Is this a reply to an existing issue?
    #
    match = ISSUE_SUBJECT_MATCH.search(message['subject'])

    # Parse message payload
    #
    body = []
    html = []
    attachments = []
    counter = 0

    for part in message.walk():

        # multipart/* are just containers
        if part.get_content_maintype() == 'multipart':
            continue

        # Applications should really sanitize the given filename so that an
        # email message can't be used to overwrite important files
        #
        if part.get_content_type() == "text/plain":
            body.append(unicode(
                part.get_payload(decode=True),
                part.get_content_charset() or "utf8",
                'ignore'
            ))
        elif part.get_content_type() == "text/html":

            if part.get_content_charset() is None:
                charset = str(chardet.detect(str(part))['encoding'])
            else:
                charset = str(part.get_content_charset())

            text = unicode(part.get_payload(decode=True), charset, "ignore")

            html.append(html2text(text).replace("&nbsp_place_holder;", " "))

        elif part.get_content_type() == "application/ms-tnef":

            tnef = TNEF(part.get_payload(decode=True), do_checksum=False)

            for tnef_att in tnef.attachments:

                att = Attachment()
                att._file = ContentFile(tnef_att.data)
                att._file.name = tnef_att.long_filename()
                att.mimetype = mimetypes.guess_type(tnef_att.long_filename())
                attachments.append(att)

        else:
            filename = part.get_filename()

            if not filename:
                ext = mimetypes.guess_extension(part.get_content_type())
                if not ext:
                    # Use a generic bag-of-bits extension
                    ext = '.bin'
                filename = 'part-%03d%s' % (counter, ext)
            counter += 1

            att = Attachment()
            att._file = ContentFile(part.get_payload(decode=True))
            att._file.name = filename
            att.mimetype = part.get_content_type()
            attachments.append(att)

    # Some emails contain both html and plain. We assume that in this case,
    # we only need the html part.
    #
    if html:
        body = "\n\n".join(html)
    else:
        body = "\n\n".join(body)

    if match:
        issue_id = int(match.groups()[0])
        issue = Issue.objects.get(pk=issue_id)

        issue.comments.create(comment=body, comment_by=sender)

        if issue.status == settings.ISSUE_STATUS_WAIT:
            issue.set_status(settings.ISSUE_STATUS_OPEN)
    else:
        issue = Issue(title=message['subject'],
                      contact=sender,
                      text=body,
                      sla=sla)

    if sla and sla.default_service:
        issue.service = sla.default_service

    issue.save()

    for att in attachments:
        att.issue = issue
        att.save()

    notify("issue_received",
           {"issue": issue},
           issue.email_from,
           from_addr)

    return True
