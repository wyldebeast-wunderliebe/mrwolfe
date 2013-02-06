from datetime import datetime
from django.test.testcases import TestCase
from django.conf import settings
from mrwolfe.models.issue import Issue
from mrwolfe.models.sla import SLA
from mrwolfe.models.contact import Contact


class IssueTest(TestCase):

    def test_in_time(self):
        
        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")
        
        service =sla.service_set.create(response_time=2,
                                        solution_time=4,
                                        priority="normal")

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()
        contact.sla.add(sla)

        issue = Issue(title="broken stuff",
                      contact=contact,
                      service=service,
                      text="Well, it's broken",
                      created=datetime.now(),
                      sla=sla)

        issue.save()

        self.assertTrue(issue.in_time)

        issue.created = datetime(1966, 1, 1, 12)

        self.assertFalse(issue.in_time)

        issue.status = settings.ISSUE_STATUS_CLOSED

        status = issue.status_history.create(name=settings.ISSUE_STATUS_CLOSED,
                                             issue=issue,
                                             comment="solved")
        
        status.date = datetime(1966, 1, 1, 14)
        status.save()

        self.assertTrue(issue.in_time)
