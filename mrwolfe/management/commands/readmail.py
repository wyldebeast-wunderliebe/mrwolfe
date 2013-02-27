import poplib
import logging
from email import parser
from django.core.management.base import NoArgsCommand
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.utils import handle_message


LOGGER = logging.getLogger("mrwolfe")


class Command(NoArgsCommand):

    help = """Read mailqueues for SLA's"""
    
    def handle(self, *args, **options):
        
        LOGGER.info("Reading mailqueues")

        for queue in MailQueue.objects.all():
            self.handle_queue(queue)

    def handle_queue(self, mailqueue):
        
        pop_conn = poplib.POP3_SSL(mailqueue.host, int(mailqueue.port or 995))
        pop_conn.user(mailqueue.usr)
        pop_conn.pass_(mailqueue.pwd)

        LOGGER.info("Handling queue %s" % mailqueue)

        nr_of_messages = len(pop_conn.list()[1])

        LOGGER.info("Fetching %s messages" % nr_of_messages)

        for i in range(nr_of_messages):
            message = "\n".join(pop_conn.retr(i+1)[1])
            
            message = parser.Parser().parsestr(message)

            # TODO: handle complex messages, with attachments and the likes...
            #
            try:
                handled = handle_message(message)

                if not handled:
                    LOGGER.warning("Unhandled message!")
            except:
                LOGGER.exception("Exception in handling message!")

        pop_conn.quit()
