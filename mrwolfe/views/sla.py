from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.sla import SLA
from mrwolfe.models.service import Service
from mrwolfe.forms.sla import SLAForm
from mrwolfe.models.issue import Issue


class SLAView(DetailView):

    model = SLA
    template_name = "view_sla.html"

    def get_context_data(self, **kwargs):

        ctx = super(SLAView, self).get_context_data(**kwargs)

        ctx.update({"view": self})

        return ctx    

    def list_services(self):

        return Service.objects.filter(sla=self.object)

    def list_my_issues(self):

        return Issue.objects.filter(sla=self.object)

    def list_open_issues(self):

        return Issue.objects.filter(sla=self.object)


class SLACreate(CreateView):

    model = SLA
    form_class = SLAForm
    template_name = "create_sla.html"

    def get_success_url(self):

        return "/config?message=SLA+aangemaakt&status=0"


class SLAJSONCreate(JSONCreateView):

    model = SLA
    form_class = SLAForm    
    success_template_name = "snippets/sla.html"


class SLAEdit(UpdateView):

    model = SLA
    form_class = SLAForm
    template_name = "edit_sla.html"

    def get_success_url(self):

        return "/config?message=SLA+gewijzigd&status=0"


class SLAJSONEdit(JSONUpdateView):

    model = SLA
    form_class = SLAForm
    success_template_name = "snippets/sla.html"


class SLADelete(DeleteView):

    model = SLA

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def get_success_url(self):

        return "/config?message=SLA+verwijderd&status=0"

class SLAJSONDelete(JSONDeleteView):

    model = SLA
