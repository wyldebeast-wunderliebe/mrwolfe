from mrwolfe.itconn.base import ITConnector
from jira.client import JIRA


class JiraConnector(ITConnector):

    def create_issue(self, issue, connector_instance):

        options = {
            'rest_api_version': 'latest',
            'server': connector_instance.uri
        }

        client = JIRA(options=options,
                      basic_auth=(connector_instance.usr,
                                  connector_instance.pwd))

        jira_issue = client.create_issue(
            project={'key': 'PROVGRON'},
            summary=issue.title,
            description=issue.text,
            issuetype={'name': 'Bug'})

        print jira_issue
