from mrwolfe.models.issue import Issue
from haystack.forms import ModelSearchForm


class SearchForm(ModelSearchForm):

    def search(self):

        if self.cleaned_data.get('q', None):
            sqs = self.searchqueryset.narrow('%s*' % self.cleaned_data['q'])
        else:
            sqs = self.searchqueryset.all()

        if self.load_all:
            sqs = sqs.load_all()

        return sqs.models(Issue)
