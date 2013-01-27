from django.views.generic import TemplateView
from mrwolfe.models.sla import SLA
from mrwolfe.models.customer import Customer
from mrwolfe.models.issue import Issue


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):

        ctx = super(IndexView, self).get_context_data(**kwargs)

        ctx.update({"view": self})

        return ctx    

    def list_my_issues(self):

        return Issue.objects.filter(assignee=self.request.user)

    def list_unassigned_issues(self):

        return Issue.objects.filter(assignee__isnull=True)

    def list_slas(self):

        return SLA.objects.all()

    def list_customers(self):

        return Customer.objects.all()

        
class AdminView(IndexView):

    template_name = "admin.html"
