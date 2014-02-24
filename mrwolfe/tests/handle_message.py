# -*- coding: utf-8 -*-

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.test.testcases import TestCase
from mrwolfe.tests.utils import NotificationsBin
from mrwolfe.utils import handle_message
from mrwolfe.models.sla import SLA
from mrwolfe.models.issue import Issue
from mrwolfe.models.rule import Rule
from mrwolfe.models.service import Service
from mrwolfe.models.contact import Contact


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
        self.simplemsg = MIMEText("<p>It's broken. 天津元/月</p>", 'html')

        self.multipartmsg['Subject'] = self.simplemsg['Subject'] = "Issue"
        self.multipartmsg['From'] = self.simplemsg['From'] = FROM
        self.multipartmsg['To'] = self.simplemsg['To'] = TO

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText("It's broken, Hyvää huomenta. 天津元/月", 'plain')
        part2 = MIMEText("<blink>Really!</blink>", 'xml')
        part3 = MIMEText(
            "Hyvää huomenta".decode("utf-8").encode("iso-8859-1"),
            'plain')
        part4 = MIMEText(
            "Hyvää huomenta".decode("utf-8").encode("iso-8859-1"),
            'html')

        self.multipartmsg.attach(part1)
        self.multipartmsg.attach(part2)
        self.multipartmsg.attach(part3)
        self.multipartmsg.attach(part4)

    def test_handle_message(self):

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        notification = NotificationsBin.receive()

        self.assertEquals([FROM], notification['to'])

    def test_handle_message_with_extended_from(self):

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        notification = NotificationsBin.receive()

        self.assertEquals([FROM], notification['to'])    
        self.assertEquals(TO, notification['from'])


    def test_handle_message_sla_with_default_service(self):

        service = Service.objects.create(sla=self.sla, priority="laag")

        self.sla.default_service = service
        self.sla.save()

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        self.assertEquals(service, self.sla.issue_set.all()[0].service)

        notification = NotificationsBin.receive()

        self.assertEquals([FROM], notification['to'])    
        self.assertEquals(TO, notification['from'])


    def test_handle_message_with_attachments(self):

        handle_message(self.multipartmsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        issue = self.sla.issue_set.all()[0]

        self.assertEquals(1, issue.attachment_set.all().count())

        notification = NotificationsBin.receive()

        self.assertEquals([FROM], notification['to'])    
        self.assertEquals(TO, notification['from'])


    def test_handle_message_with_existing_issue(self):

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        issue = self.sla.issue_set.all()[0]

        self.simplemsg.replace_header('subject', "Re: %s" % issue.issue_id)

        handle_message(self.simplemsg)

        self.assertEquals(1, self.sla.issue_set.all().count())

        self.assertEquals(1, issue.comments.all().count())

        notification = NotificationsBin.receive()

        self.assertEquals([FROM], notification['to'])    
        self.assertEquals(TO, notification['from'])


    def test_handle_bouncing_issue(self):

        msg = MIMEText("It's broken", 'plain')

        msg['From'] = "dr.evil@undergroundlair.com"
        msg['To'] = "support@evilempire.com"
        msg['Subject'] = "help!"

        import mrwolfe.utils as utils
        utils.settings.ALLOW_NON_CONTACTS = False

        handle_message(msg)

        self.assertEquals(0, Issue.objects.all().count())

        notification = NotificationsBin.receive()

        self.assertEquals("Invalid contact for support", 
                          notification['subject'])


    def test_handle_winmail_dat(self):

        msg = MIMEMultipart('alternative')

        msg['Subject'] = self.simplemsg['Subject'] = "Issue"
        msg['From'] = self.simplemsg['From'] = FROM
        msg['To'] = self.simplemsg['To'] = TO

        winmaildat = os.path.join(os.path.dirname(__file__), "winmail.dat")

        msg.attach(MIMEApplication(file(winmaildat).read(), "ms-tnef"))

        handle_message(msg)

        issue = self.sla.issue_set.all()[0]

        self.assertEquals(1, issue.attachment_set.all().count())

        self.assertTrue(issue.attachment_set.all()[0].is_image)
