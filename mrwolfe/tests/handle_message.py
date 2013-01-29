from django.test.testcases import TestCase
from mrwolfe.utils import handle_message
from mrwolfe.models.sla import SLA
from mrwolfe.models.rule import Rule
from mrwolfe.models.service import Service
from mrwolfe.models.contact import Contact
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TO = "support@evilempire.com"
FROM = "dokter@evilempire.com"


class HandleMessageTest(TestCase):

    def setUp(self):

        super(HandleMessageTest, self).setUp()

        self.sla = SLA.objects.create(name="RoadMap",
                                      start_date="2012-01-01",
                                      end_date="2012-12-31")

        rule = Rule.objects.create(field="from",
                                   regexp="dokter",
                                   sla=self.sla)

        contact = Contact.objects.create(email="dokter@evilempire.com")
        
        contact.save()
        contact.sla.add(self.sla)

        # Create message container - the correct MIME type is
        # multipart/alternative.
        self.multipartmsg = MIMEMultipart('alternative')
        self.simplemsg = MIMEText("It's broken", 'plain')

        self.multipartmsg['Subject'] = self.simplemsg['Subject'] = "Issue"
        self.multipartmsg['From'] = self.simplemsg['From'] = FROM
        self.multipartmsg['To'] = self.simplemsg['To'] = TO

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText("It's broken", 'plain')
        part2 = MIMEText("<blink>Really!</blink>", 'html')

        self.multipartmsg.attach(part1)
        self.multipartmsg.attach(part2)

    def test_handle_message(self):

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())


    def test_handle_message_with_extended_from(self):

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

    
    def test_handle_message_sla_with_default_service(self):

        service = Service.objects.create(sla=self.sla, priority="laag")

        self.sla.default_service = service
        self.sla.save()

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        self.assertEquals(service, self.sla.issue_set.all()[0].service)

    def test_handle_message_with_attachments(self):

        handle_message(self.multipartmsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        issue = self.sla.issue_set.all()[0]

        self.assertEquals(1, issue.attachment_set.all().count())
