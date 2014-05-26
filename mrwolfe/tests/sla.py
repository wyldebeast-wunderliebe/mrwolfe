from django.test.testcases import TestCase
from mrwolfe.models.sla import SLA
from mrwolfe.models.contact import Contact


class SLATest(TestCase):

    def test_is_contact(self):
        
        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")
        
        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()
        contact.sla.add(sla)

        self.assertTrue(sla.is_contact(contact))

        contact.sla.remove(sla)

        self.assertFalse(sla.is_contact(contact))
