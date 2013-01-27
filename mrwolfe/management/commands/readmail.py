import poplib
import logging
import re
from email import parser
from django.conf import settings
from django.core.management.base import NoArgsCommand
from mrwolfe.models.sla import SLA
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.models.issue import Issue
from mrwolfe.utils import determine_sla


ISSUE_SUBJECT_MATCH = re.compile('#([0-9]{8})')
LOGGER = logging.getLogger("mrwolfe")


class Command(NoArgsCommand):

    help = """Read mailqueues for SLA's"""
    
    def handle(self, *args, **options):
        
        LOGGER.info("Reading mailqueues")

        for queue in MailQueue.objects.all():
            self.handle_queue(queue)

    def handle_sla(self, mailqueue):
        
        pop_conn = poplib.POP3_SSL(mailqueue.host, mailqueue.port or 110)
        pop_conn.user(mailqueue.usr)
        pop_conn.pass_(mailqueue.pwd)

        LOGGER.info("Handling queue %" % mailqueue)

        nr_of_messages = len(pop_conn.list()[1])

        LOGGER.info("Fetching %s messages" % nr_of_messages)

        for i in range(nr_of_messages):
            message = "\n".join(pop_conn.retr(i+1)[1])
            
            message = parser.Parser().parsestr(message)

            try:
                if mailqueue.sla_set.all().count() == 1:
                    sla = mailqueue.sla_set.all()[0]
                else:
                    sla = determine_sla(message)

                sender = Contact.objects.filter(
                    "user__email"=message['sender'])[0]

                if sla.is_contact(sender) or settings.ALLOW_NON_CONTACTS:
                    
                    match = ISSUE_SUBJECT_MATCH.search(message['subject'])

                    if match:
                        issue_id = int(match.groups()[0])
                        issue = Issue.objects.get(pk=issue_id)

                        issue.add_comment(message.get_payload())
                    else:
                        issue = Issue(title=message['subject'],
                                      contact=sender,
                                      text=message.get_payload(),
                                      sla=sla)
                    issue.save()
            except:

                # bounce!

                pass

        pop_conn.quit()
