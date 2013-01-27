from mrwolfe.models.contact import Contact
from mrwolfe.models.sla import SLA


def determine_sla(message):

    """ Determine to what SLA this email message is addressed. Return None
    if this cannot be determined. The email_message is a parsed message
    as per email.parser """

    # first round, try sender. If this leads to a single SLA, this is the one.
    #
    try:
        sender = Contact.objects.filter(user__email=message['sender'])[0]

        slas = SLA.objects.filter(customer=sender.customer)

        if slas.count() == 1:
            return slas[0]
    except:
        pass

    return None
