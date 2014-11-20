import logging
from email import parser
from django.core.management.base import NoArgsCommand
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.utils import handle_message
from mrwolfe.mailutils import POPService, IMAPService


LOGGER = logging.getLogger("mrwolfe")


class Command(NoArgsCommand):

    help = """Read mailqueues for SLA's"""

    def handle(self, *args, **options):

        LOGGER.info("Reading mailqueues")

        for queue in MailQueue.objects.all():
            self.handle_queue(queue)

    def handle_queue(self, mailqueue):

        LOGGER.info("Handling queue %s" % mailqueue)

        if mailqueue.protocol == 0:
            service = POPService(mailqueue.host, int(mailqueue.port or 995))
        else:
            service = IMAPService(mailqueue.host, int(mailqueue.port or 143))

        LOGGER.debug("Protocol used: %s" %
                     (mailqueue.protocol and "IMAP" or "POP"))

        service.auth(mailqueue.usr, mailqueue.pwd)

        cnt = 0
        unhandled = []

        for msg_id, message in service.list():

            try:
                handled = handle_message(message)

                if not handled:
                    LOGGER.warning("Unhandled message!")
                    unhandled.append(msg_id)
                else:
                    cnt += 1
            except:
                LOGGER.exception("Exception in handling message!")
                unhandled.append(msg_id)

        service.mark_unread(unhandled)

        LOGGER.info("Handled %i messages" % cnt)

        service.quit()
