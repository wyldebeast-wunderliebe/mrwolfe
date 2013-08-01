import datetime
from haystack import indexes
from mrwolfe.models import Issue


class IssueIndex(indexes.SearchIndex):

    text = indexes.CharField(document=True, use_template=True,
                             template_name="search/indexes/issue_index.txt")
    issue_id = indexes.CharField()

    def get_model(self):
        return Issue
