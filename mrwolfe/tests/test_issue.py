from datetime import datetime
from django.test.testcases import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from mrwolfe.models.issue import Issue
from mrwolfe.models.sla import SLA
from mrwolfe.models.contact import Contact
from mrwolfe.models.operator import Operator
from mrwolfe.tests.utils import NotificationsBin


class IssueTest(TestCase):

    def setUp(self):

        NotificationsBin.clear()
        user = User.objects.create(username="dzjengis", is_superuser=False)
        Operator.objects.create(user=user, email="dzjengis@khan.org")

    def test_in_time(self):

        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")

        service = sla.service_set.create(
            response_time=2, solution_time=4, priority="normal")

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()
        contact.sla.add(sla)

        issue = Issue(title="broken stuff",
                      contact=contact,
                      service=service,
                      text="Well, it's broken",
                      created=timezone.now(),
                      sla=sla)

        issue.save()

        self.assertTrue(issue.in_time)

        issue.created = timezone.make_aware(
            datetime(1966, 1, 1, 12), timezone.get_default_timezone())

        self.assertFalse(issue.in_time)

        issue.status = settings.ISSUE_STATUS_CLOSED

        status = issue.status_history.create(name=settings.ISSUE_STATUS_CLOSED,
                                             issue=issue,
                                             comment="solved")

        status.date = timezone.make_aware(
            datetime(1966, 1, 1, 14), timezone.get_default_timezone())
        status.save()

        self.assertTrue(issue.in_time)

    def test_email_from(self):

        sla = SLA.objects.create(name="RoadMap",
                                 start_date="2012-01-01",
                                 end_date="2012-12-31")

        service = sla.service_set.create(
            response_time=2, solution_time=4, priority="normal")

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()
        contact.sla.add(sla)

        issue = Issue(title="broken stuff",
                      contact=contact,
                      text="Well, it's broken")

        issue.save()

        self.assertEquals(settings.DEFAULT_FROM_ADDR, issue.email_from)

        issue.sla = sla

        self.assertEquals(settings.DEFAULT_FROM_ADDR, issue.email_from)

        sla.email_from = "bob@dobalina.org"

        self.assertEquals("bob@dobalina.org", issue.email_from)

    def test_time_on_hold(self):

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()

        issue = Issue(title="broken stuff",
                      contact=contact,
                      text="Well, it's broken")

        issue.save()

        self.assertEquals(0, issue._time_on_hold)

        status = issue.status_history.create(name=settings.ISSUE_STATUS_HOLD,
                                             issue=issue,
                                             comment="no comment")
        status.date = timezone.make_aware(
            datetime(2000, 1, 1, 16, 33), timezone.get_default_timezone())
        status.save()

        status = issue.status_history.create(name=settings.ISSUE_STATUS_OPEN,
                                             issue=issue,
                                             comment="no comment")

        status.date = timezone.make_aware(
            datetime(2000, 1, 1, 16, 37), timezone.get_default_timezone())
        status.save()

        status = issue.status_history.create(name=settings.ISSUE_STATUS_HOLD,
                                             issue=issue,
                                             comment="no comment")
        status.date = timezone.make_aware(
            datetime(2000, 1, 1, 17, 33), timezone.get_default_timezone())
        status.save()

        status = issue.status_history.create(name=settings.ISSUE_STATUS_OPEN,
                                             issue=issue,
                                             comment="no comment")

        status.date = timezone.make_aware(
            datetime(2000, 1, 1, 18, 37), timezone.get_default_timezone())
        status.save()

        self.assertEquals(60 * 68, issue._time_on_hold)

    def test_notification(self):

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()

        issue = Issue.objects.create(
            title="broken stuff", contact=contact,
            text="Well, it's really broken")

        issue.save()

        notification = NotificationsBin.receive()

        issue_url = reverse(
            'view_issue', args=[], kwargs={'pk': issue.pk})

        self.assertTrue(issue_url in notification["body"])

    def test_clone(self):

        """ deep clone """

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()

        issue = Issue.objects.create(
            title="broken stuff", contact=contact,
            text="Well, it's really broken")

        issue.comments.create(comment="Really?")
        issue.comments.create(comment="Really, really?")

        self.assertTrue(issue.can_clone)

        clone = issue.clone()

        self.assertEquals(issue.comments.all().count(),
                          clone.comments.all().count())
