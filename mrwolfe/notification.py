import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from email.parser import Parser
from mrwolfe.models.setting import Setting


LOGGER = logging.getLogger("mrwolfe")


def notify(notification_id, context, from_addr, to_addr):

    """ Send out notification. Or don't... """

    if Setting.objects.filter(name='notification').exists() and \
       Setting.objects.get(name='notification').value == "off":
        LOGGER.warning("Notification seems to be disabled")
        return

    # Check on to address, whether it contains our own
    # mailbox. Sending to self is generally a Bad Idea (tm), as we
    # found out some day...
    #
    if to_addr == from_addr:
        LOGGER.warning("To and From addresses are the same."
                       "Not sending notification..!")
        return

    # to_addr = ", ".join(filter(
    #     lambda x: x not in settings.NOTIFICATION_BLACKLIST,
    #     to_addr.split(", ")))

    to_list = to_addr.split(", ")
    to_addr = []
    for addr in to_list:
        blacklisted = False
        for mofo in settings.NOTIFICATION_BLACKLIST:
            if mofo in addr:
                blacklisted = True
        if not blacklisted:
            to_addr.append(addr)
    to_addr = ", ".join(to_addr)

    if not to_addr:
        LOGGER.error("No 'to' address set; bye now")
        return

    template = settings.NOTIFICATION_MAP.get(
        notification_id, "notification/%s.html" % notification_id)

    context.update({"from": from_addr or settings.DEFAULT_FROM_ADDR,
                    "to": to_addr})

    if not template:
        LOGGER.error("No template found for %s" % notification_id)
        return

    try:
        message = render_to_string(template, context).encode("utf-8")

        email_message = Parser().parsestr(message)

        LOGGER.debug("Sending out notification %s to %s" % (notification_id, email_message['to']))

        send_mail(email_message['subject'],
                  email_message.get_payload(),
                  email_message['from'],
                  email_message['to'].split(","),
                  fail_silently=False)
    except:
        try:
            LOGGER.warning("Couldn't render template, trying simple message")

            send_mail(email_message['subject'],
                      "An issue has been created",
                      email_message['from'],
                      email_message['to'].split(","),
                      fail_silently=False)
        except:
            LOGGER.exception("No mail sent")
