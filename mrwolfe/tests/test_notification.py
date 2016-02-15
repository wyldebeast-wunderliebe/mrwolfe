# -*- coding: utf-8 -*-

from django.test.testcases import TestCase
from django.conf import settings
from mrwolfe.tests.utils import NotificationsBin
from mrwolfe.notification import notify


class TestIssue(object):

    issue_id = "foo"
    title = "Foo"
    text = "Foo foo foo 天津元/月</p>"
    url = "http://foo.org/foo"


class NotificationTest(TestCase):

    def setUp(self):

        NotificationsBin.clear()

    def test_notify(self):

        settings.NOTIFICATION_BLACKLIST = ["bob@dobalina.org", 
                                           "drevil@evilempire.net"]

        context = {"from": "bob@dobalina.org", 
                   "to": "bob@dobalina.org", 
                   "issue": TestIssue()}

        notify("issue_created", context, "bob@dobalina.org", "bob@dobalina.org")

        try:
            notification = NotificationsBin.receive()
            self.fail("We should not have mail!")
        except:
            pass

        notify("issue_created", context, "bob@dobalina.org", 
               "bob@dobalina.org, drevil@evilempire.net")

        try:
            notification = NotificationsBin.receive()
            self.fail("We should not have mail!")
        except:
            pass

        notify("issue_created", context, "bob@dobalina.org", 
               "bob@dobalina.org, batman@evilempire.net")

        try:
            notification = NotificationsBin.receive()
        except:
            self.fail("We should have mail!")

        # reset...
        settings.NOTIFICATION_BLACKLIST = []
