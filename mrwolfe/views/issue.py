from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings
from pu_in_content.views.jsonbase import JSONUpdateView
from mrwolfe.models.issue import Issue
from mrwolfe.models.status import Status
from mrwolfe.models.sla import SLA
from mrwolfe.models.operator import Operator
from mrwolfe.forms.issue import IssueForm
from base import BaseView


class IssueView(BaseView):

    model = Issue

    def status_history(self):

        return Status.objects.filter(issue=self.object)

    def list_status_options(self):

        return (opt for opt in settings.ISSUE_STATUS_CHOICES \
                    if opt[0] != self.object.status)

    def list_operators(self):

        return Operator.objects.all().exclude(user=self.object.assignee)


class IssueHistoryView(BaseView):

    model = Issue
    template_name = "snippets/history.html"

    def status_history(self):

        return Status.objects.filter(issue=self.object)


class IssueCreate(CreateView):

    model = Issue
    form_class = IssueForm
    template_name = "create_issue.html"

    def get_initial(self):

        initial = super(CreateView, self).get_initial()

        if "sla" in self.request.GET:
            initial["sla"] = self.request.GET["sla"]

        return initial

    def get_form(self, form_class):
        
        form = super(CreateView, self).get_form(form_class)

        if "sla" in self.request.GET:

            form.fields["priority"].queryset = SLA.objects.get(pk=self.request.GET["sla"]).service_set.all()

        return form

    def get_success_url(self):

        return "/?message=Issue+aangemaakt&status=0"


class IssueAssigneeJSONEdit(JSONUpdateView):

    model = Issue
    form_class = IssueForm
    success_template_name = "controls/assignee_control.html"

    def get_context_data(self, **kwargs):
        
        ctx = super(IssueAssigneeJSONEdit, self).get_context_data(**kwargs)
        
        ctx.update({"view": self})
        
        return ctx    

    def list_operators(self):

        return Operator.objects.all().exclude(user=self.object.assignee)


class IssueEdit(UpdateView):

    model = Issue
    form_class = IssueForm
    template_name = "edit_issue.html"

    def get_success_url(self):

        return "/?message=Issue+gewijzigd&status=0"


class IssueDelete(DeleteView):

    model = Issue

    def get_success_url(self):

        return "/?message=Issue+verwijderd&status=0"
