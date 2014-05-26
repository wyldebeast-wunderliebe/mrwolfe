import json
from markdown import markdown
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.issue import Issue
from mrwolfe.models.status import Status
from mrwolfe.models.sla import SLA
from mrwolfe.models.operator import Operator
from mrwolfe.forms.issue import IssueForm, IssueAssigneeForm
from base import BaseView


class IssueView(BaseView):

    model = Issue

    def status_history(self):

        return Status.objects.filter(issue=self.object)

    def list_status_options(self):

        return (opt for opt in settings.ISSUE_STATUS_CHOICES
                if opt[0] != self.object.status)

    def list_users(self):

        users = Operator.objects.all()

        if self.object.assignee:
            users = users.exclude(id=self.object.assignee.id)

        return users

    @property
    def text(self):

        return mark_safe(markdown(self.object.text))


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

        initial = super(IssueCreate, self).get_initial()

        if "sla" in self.request.GET:
            initial["sla"] = self.request.GET["sla"]

        return initial

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('submit', '') == "Cancel":
            return HttpResponseRedirect("/")
        else:
            return super(IssueCreate, self).post(request, *args, **kwargs)

    def get_form(self, form_class):

        form = super(IssueCreate, self).get_form(form_class)

        if "sla" in self.request.GET:

            form.fields["service"].queryset = SLA.objects.get(
                pk=self.request.GET["sla"]).service_set.all()

        return form

    def get_success_url(self):

        return "/?message=Issue+created&status=0"


class UpdateIssueAssignee(UpdateView):

    model = Issue
    form_class = IssueAssigneeForm
    template_name = "controls/assignee_control.html"

    def get_form_kwargs(self):

        return {'data': self.request.GET, 'instance': self.object}

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.update()

        return super(UpdateIssueAssignee, self).get(request, *args, **kwargs)

    def list_users(self):

        users = Operator.objects.all()

        if self.object.assignee:
            users = users.exclude(id=self.object.assignee.id)

        return users


class IssueClone(DetailView):

    model = Issue

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        clone = self.object.clone()

        if clone:

            context = {"status": 0,
                       "message": "Your issue has been cloned to %s" %
                       clone.issue_id}
        else:
            context = {"status": -1,
                       "message": "Not cloned!"}

        return HttpResponse(json.dumps(context),
                            content_type="application/json")


class IssueEdit(UpdateView):

    model = Issue
    form_class = IssueForm
    template_name = "edit_issue.html"

    def get_success_url(self):

        return "/?message=Issue+updated&status=0"

    def post(self, request, *args, **kwargs):

        return super(IssueEdit, self).post(request, *args, **kwargs)

    @property
    def cancel_url(self):

        return "/"


class DeleteIssue(DeleteView):

    model = Issue
    template_name = "snippets/confirm_delete_issue.html"
    success_url = reverse_lazy("config")
