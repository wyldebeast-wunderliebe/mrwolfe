import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from email.parser import Parser


LOGGER = logging.getLogger("mrwolfe")


def notify(notification_id, context, from_addr, to_addr):

    """ Send out notification. """

    template = settings.NOTIFICATION_MAP.get(notification_id, None)

    context.update({"from": from_addr, "to": to_addr})

    if not template:
        LOGGER.error("No template found for %s" % notification_id)
    else:
        try:
            message = render_to_string(template, context)

            email_message = Parser().parsestr(message)

            send_mail(email_message['subject'], 
                      email_message.get_payload(), 
                      email_message['from'],
                      [email_message['to']],
                      fail_silently=False)
        except:
            LOGGER.exception("Couldn't render template")
