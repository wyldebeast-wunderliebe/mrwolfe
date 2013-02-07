import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from email.parser import Parser


LOGGER = logging.getLogger("mrwolfe")


def notify(notification_id, context, from_addr, to_addr):

    """ Send out notification. """

    if not to_addr:
        LOGGER.error("No 'to' address set; bye now")
        return 

    template = settings.NOTIFICATION_MAP.get(notification_id, 
                                             "notification/%s.html" % \
                                                 notification_id)

    context.update({"from": from_addr or settings.DEFAULT_FROM_ADDR, 
                    "to": to_addr})

    if not template:
        LOGGER.error("No template found for %s" % notification_id)
        return

    try:
        message = render_to_string(template, context)
        
        email_message = Parser().parsestr(message)

        LOGGER.debug("Sending out notification %s to %s" % \ 
                     (notification_id, email_message['to']))
        
        send_mail(email_message['subject'], 
                  email_message.get_payload(), 
                  email_message['from'],
                  email_message['to'].split(","),
                  fail_silently=False)
    except:
        LOGGER.exception("Couldn't render template, no mail sent")
