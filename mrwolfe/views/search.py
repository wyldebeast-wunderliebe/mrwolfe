from django.conf import settings
from django.views.generic import TemplateView
from haystack.views import SearchView
from mrwolfe.models.issue import Issue


class SearchView(SearchView):

    template_name = "search.html"

    def get_context_data(self, **kwargs):

        ctx = super(IndexView, self).get_context_data(**kwargs)

        ctx.update({"view": self})

        return ctx    

    def object_list(self):

        qry = self.request.REQUEST['qry']

