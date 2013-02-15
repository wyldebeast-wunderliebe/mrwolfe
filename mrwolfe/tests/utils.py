class NotificationsBin(object):

    _notifications = []

    @staticmethod
    def send(subject, body, _from, to, fail_silently=False):

        NotificationsBin._notifications.append(
            {"subject": subject, "body": body, "from": _from, "to": to})

    @staticmethod
    def receive():

        return NotificationsBin._notifications[-1]


print "Monkey patching send_mail"
import mrwolfe.notification as notification
notification.send_mail = NotificationsBin.send
