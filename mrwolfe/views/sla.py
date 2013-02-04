from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.sla import SLA
from mrwolfe.models.rule import Rule
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

    def list_rules(self):

        return Rule.objects.filter(sla=self.object)

    def nr_of_issues_in_time(self):

        return len([i for i in self.object.issue_set where i.in_time])

    def perc_of_issues_in_time(self):

        return (len([i for i in self.object.issue_set where i.in_time]) / \
                    self.object.issue_set.count()) * 100


class SLACreate(CreateView):

    model = SLA
    form_class = SLAForm
    template_name = "create_sla.html"

    def get_form(self, form_class):

        form = super(SLAJSONEdit, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form

    def get_success_url(self):

        return "/config?message=SLA+aangemaakt&status=0"


class SLAJSONCreate(JSONCreateView):

    model = SLA
    form_class = SLAForm    
    success_template_name = "snippets/sla.html"

    def get_form(self, form_class):

        form = super(SLAJSONEdit, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form


class SLAEdit(UpdateView):

    model = SLA
    form_class = SLAForm
    template_name = "edit_sla.html"

    def get_form(self, form_class):

        form = super(SLAJSONEdit, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form

    def get_success_url(self):

        return "/config?message=SLA+gewijzigd&status=0"


class SLAJSONEdit(JSONUpdateView):

    model = SLA
    form_class = SLAForm
    success_template_name = "snippets/sla.html"

    def get_form(self, form_class):

        form = super(SLAJSONEdit, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form


class SLADelete(DeleteView):

    model = SLA

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def get_success_url(self):

        return "/config?message=SLA+verwijderd&status=0"

class SLAJSONDelete(JSONDeleteView):

    model = SLA
