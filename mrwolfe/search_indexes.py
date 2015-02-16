from haystack import indexes
from mrwolfe.models import Issue


class IssueIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
        template_name="search/indexes/issue_index.txt",
        model_attr="text")

    issue_id = indexes.CharField(model_attr="issue_id")

    def get_model(self):
        return Issue
