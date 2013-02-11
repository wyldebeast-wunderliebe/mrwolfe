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

        return self.object.service_set.all()

    def list_contacts(self):

        return self.object.contact_set.all()

    def list_rules(self):

        return self.object.rule_set.all()

    def nr_of_issues(self):

        return self.object.issue_set.count()

    def nr_of_issues_late(self):

        return len([i for i in self.object.issue_set.all() if not i.in_time])

    def perc_of_issues_late(self):

        try:
            return "%.1f" % ((self.nr_of_issues_late() / \
                                  float(self.object.issue_set.count())) * 100)
        except:
            return "-"


class SLACreate(CreateView):

    model = SLA
    form_class = SLAForm
    template_name = "create_sla.html"

    def get_form(self, form_class):

        form = super(SLACreate, self).get_form(form_class)

        form.fields['default_service'].queryset = Service.objects.none()

        return form

    def get_success_url(self):

        return "/config?message=SLA+created&status=0"


class SLAJSONCreate(JSONCreateView):

    model = SLA
    form_class = SLAForm    
    success_template_name = "snippets/sla.html"

    def get_form(self, form_class):

        form = super(SLAJSONCreate, self).get_form(form_class)

        form.fields['default_service'].queryset = Service.objects.none()

        return form


class SLAEdit(UpdateView):

    model = SLA
    form_class = SLAForm
    template_name = "edit_sla.html"

    def get_form(self, form_class):

        form = super(SLAEdit, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form

    def get_success_url(self):

        return "/config?message=SLA+updated&status=0"


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

        return "/config?message=SLA+removed&status=0"

class SLAJSONDelete(JSONDeleteView):

    model = SLA
