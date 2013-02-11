from markdown import markdown
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView, UpdateView
from django.conf import settings
from django.http import HttpResponseRedirect
from pu_in_content.views.jsonbase import JSONUpdateView, JSONDetailView
from mrwolfe.models.issue import Issue
from mrwolfe.models.status import Status
from mrwolfe.models.sla import SLA
from mrwolfe.models.user import User
from mrwolfe.forms.issue import IssueForm
from base import BaseView


class IssueView(BaseView):

    model = Issue

    def status_history(self):

        return Status.objects.filter(issue=self.object)

    def list_status_options(self):

        return (opt for opt in settings.ISSUE_STATUS_CHOICES \
                    if opt[0] != self.object.status)

    def list_users(self):

        users = User.objects.all()

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

            form.fields["service"].queryset = SLA.objects.get(pk=self.request.GET["sla"]).service_set.all()

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

    def list_users(self):

        users = User.objects.all()

        if self.object.assignee:
            users = users.exclude(id=self.object.assignee.id)

        return users


class IssueJSONClone(JSONDetailView):

    model = Issue
    
    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        clone = self.object.clone()

        context = {"status": 0,
                   "message": "Your issue has been cloned to %s" % clone.issue_id}

        return self.render_to_response(context)


class IssueEdit(UpdateView):

    model = Issue
    form_class = IssueForm
    template_name = "edit_issue.html"

    def get_success_url(self):

        return "/?message=Issue+gewijzigd&status=0"

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('submit', '') == "Cancel":
            return HttpResponseRedirect("/")    
        else:            
            return super(IssueEdit, self).post(request, *args, **kwargs)
