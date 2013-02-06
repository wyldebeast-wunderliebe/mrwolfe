import re
import mimetypes
from html2text import html2text
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

    if re.search('<[^>]*>', from_addr):
        from_addr = re.search('<([^>]*)>', from_addr).groups(0)[0]

    if not Contact.objects.filter(email=from_addr).exists():
        if settings.ALLOW_NON_CONTACTS:
            sender = Contact.objects.create(email=from_addr)
        else:
            return False
    else:
        sender = Contact.objects.filter(email=from_addr)[0]

    if sla and not sla.is_contact(sender) and not \
            settings.ALLOW_NON_CONTACTS:
        return False
                
    # Is this a reply to an existing issue?
    #
    match = ISSUE_SUBJECT_MATCH.search(message['subject'])

    # Parse message payload
    #
    body = []
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
            body.append(part.get_payload(decode=True))
        elif part.get_content_type() == "text/html":
            body.append(html2text(part.get_payload(decode=True)))
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

    body = "\n\n".join(body)

    if match:
        issue_id = int(match.groups()[0])
        issue = Issue.objects.get(pk=issue_id)
        
        issue.comments.create(comment=body)
    else:
        issue = Issue(title=message['subject'],
                      contact=sender,
                      text=body,
                      email_from=message['to'],
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


