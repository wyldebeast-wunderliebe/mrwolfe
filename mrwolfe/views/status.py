from pu_in_content.views.jsonbase import JSONCreateView
from mrwolfe.models.status import Status
from mrwolfe.models.issue import Issue
from mrwolfe.forms.status import StatusForm
from django.conf import settings


class StatusJSONCreate(JSONCreateView):

    model = Status
    form_class = StatusForm
    success_template_name = "status_control.html"

    def get_context_data(self, **kwargs):
        
        ctx = super(StatusJSONCreate, self).get_context_data(**kwargs)
        
        ctx.update({"view": self,
                    "object": Issue.objects.get(pk=self.kwargs['issue_pk'])})
        
        return ctx

    def get_initial(self):

        return {'issue': self.kwargs['issue_pk'],
                'name': self.request.GET.get('status', '')}

    def list_status_options(self):

        return (opt for opt in settings.ISSUE_STATUS_CHOICES \
                    if opt[0] != self.object.name)
