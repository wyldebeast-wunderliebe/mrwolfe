from datetime import datetime
from django.test.testcases import TestCase
from django.conf import settings
from mrwolfe.tests.utils import NotificationsBin
from mrwolfe.models import Issue, SLA, Contact, Status


class StatusTest(TestCase):

    def setUp(self):

        NotificationsBin.clear()

        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")
        
        service =sla.service_set.create(response_time=2,
                                        solution_time=4,
                                        priority="normal")

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()
        contact.sla.add(sla)

        self.issue = Issue(title="broken stuff",
                           contact=contact,
                           service=service,
                           text="Well, it's broken",
                           created=datetime.now(),
                           sla=sla)

        self.issue.save()


    def test_notify(self):

        status = Status.objects.create(
            name=settings.ISSUE_STATUS_CLOSED,
            issue=self.issue,
            comment="Closed!")

        status.save()

        try:
            notification = NotificationsBin.receive()
        except:
            self.fail("We should have mail!")
