from django.test.testcases import TestCase
from mrwolfe.utils import determine_sla
from mrwolfe.models.sla import SLA
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.models.rule import Rule


class DetermineSLATest(TestCase):

    def setUp(self):

        super(DetermineSLATest, self).setUp()

        mq = MailQueue.objects.create(usr="bobdobalina", 
                                      pwd="xxx666", 
                                      host="pop.evilempire.org")

        self.sla0 = SLA.objects.create(name="RoadMap",
                                       start_date="2012-01-01",
                                       end_date="2012-12-31",
                                       mailqueue=mq)

        rule0 = Rule.objects.create(field="sender",
                                    regexp="pipo",
                                    sla=self.sla0)
        
        rule1 = Rule.objects.create(field="sender",
                                    regexp="dokter",
                                    sla=self.sla0)

    def test_determine_sla(self):

        message = {'sender': 'dokter@w20e.com', 'subject': 'lala'}

        self.assertEquals(self.sla0, determine_sla(message))
