from django.test.testcases import TestCase
from mrwolfe.models.rule import Rule
from mrwolfe.models.sla import SLA


class RuleTest(TestCase):

    def test_matches(self):
        
        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")
        
        rule = Rule.objects.create(field="sender",
                                   regexp="okter",
                                   sla=sla)
    
        message = {"sender": "dokter@w20e.com", "to": "support@w20e.com"}

        self.assertTrue(rule.matches(message))
        
        message['sender'] = "pipo@w20e.com"

        self.assertFalse(rule.matches(message))
