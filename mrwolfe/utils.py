import re
from django.conf import settings
from mrwolfe.models.contact import Contact
from mrwolfe.models.sla import SLA
from mrwolfe.models.issue import Issue


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
        from_addr = re.search('<([^>]*)>', 'Dok <dokter@w20e.com>').groups(0)[0]

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

    if match:
        issue_id = int(match.groups()[0])
        issue = Issue.objects.get(pk=issue_id)
        
        self.comment_set.create(comment=message.get_payload())
    else:
        issue = Issue(title=message['subject'],
        contact=sender,
        text=message.get_payload(),
        sla=sla)
    issue.save()

    return True
