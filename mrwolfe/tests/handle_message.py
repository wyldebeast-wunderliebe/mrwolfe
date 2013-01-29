from django.test.testcases import TestCase
from mrwolfe.utils import handle_message
from mrwolfe.models.sla import SLA
from mrwolfe.models.rule import Rule
from mrwolfe.models.service import Service
from mrwolfe.models.contact import Contact


class TestMessage(dict):

    def __init__(self, text, **kwargs):

        self.text = text

        for key in kwargs.keys():
            self[key.lower()] = kwargs[key]

    def get_payload(self):

        return self.text


class HandleMessageTest(TestCase):

    def setUp(self):

        super(HandleMessageTest, self).setUp()

        self.sla = SLA.objects.create(name="RoadMap",
                                      start_date="2012-01-01",
                                      end_date="2012-12-31")

        rule = Rule.objects.create(field="from",
                                   regexp="dokter",
                                   sla=self.sla)

        contact = Contact.objects.create(email="dokter@w20e.com")
        
        contact.save()
        contact.sla.add(self.sla)


    def test_handle_message(self):

        message = TestMessage("lala", From='dokter@w20e.com', Subject='lala')

        handle_message(message)

        self.assertEquals(1, self.sla.issue_set.all().count())


    def test_handle_message_with_extended_from(self):

        message = TestMessage("lala", From='Duco Dokter <dokter@w20e.com>', 
                              Subject='lala')

        handle_message(message)

        self.assertEquals(1, self.sla.issue_set.all().count())

    
    def test_handle_message_sla_with_default_service(self):

        service = Service.objects.create(sla=self.sla, priority="laag")

        self.sla.default_service = service
        self.sla.save()

        message = TestMessage("lala", From='Duco Dokter <dokter@w20e.com>', 
                              Subject='lala')

        handle_message(message)

        self.assertEquals(1, self.sla.issue_set.all().count())

        self.assertEquals(service, self.sla.issue_set.all()[0].service)
