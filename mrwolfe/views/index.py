from django.views.generic import TemplateView
from mrwolfe.models.sla import SLA
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.models.issue import Issue
from mrwolfe.models.operator import Operator
from mrwolfe.models.contact import Contact


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

        
class AdminView(IndexView):

    template_name = "admin.html"

    def list_slas(self):

        return SLA.objects.all()

    def list_mailqueues(self):

        return MailQueue.objects.all()

    def list_operators(self):

        return Operator.objects.all()

    def list_contacts(self):

        return Contact.objects.all()
