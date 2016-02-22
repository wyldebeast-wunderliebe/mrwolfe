from datetime import datetime
from django.test.testcases import TestCase
from mrwolfe.models.issue import Issue
from mrwolfe.models.contact import Contact
from mrwolfe.models.itconnector import ITConnector
from mrwolfe.itconn.jiraconnector import JiraConnector


class ITCTest(TestCase):

    def test_create_issue(self):

        contact = Contact.objects.create(email="bob@dobalina.org")
        contact.save()

        issue = Issue(title="broken stuff",
                      contact=contact,
                      text="Well, it's broken",
                      created=datetime.now())

        issue.save()

        connector = ITConnector(name="jira", connector_type="jira",
                                uri="http://issues-pg.pythonunited.com",
                                usr="d.dokter", pwd="Wagner01")

        jira_connector = JiraConnector()

        # HUUB: don't create issue in jira, too much jira spam
        # jira_connector.create_issue(issue, connector)
