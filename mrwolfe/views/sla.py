from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.sla import SLA
from mrwolfe.models.service import Service
from mrwolfe.forms.sla import SLAForm


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


class CreateSLA(CreateView):

    model = SLA
    form_class = SLAForm
    template_name = "create_sla.html"

    def get_form(self, form_class=SLAForm):

        form = super(CreateSLA, self).get_form(form_class)

        form.fields['default_service'].queryset = Service.objects.none()

        return form


class UpdateSLA(UpdateView):

    model = SLA
    form_class = SLAForm
    template_name = "edit_sla.html"

    def get_form(self, form_class=SLAForm):

        form = super(UpdateSLA, self).get_form(form_class)

        form.fields['default_service'].queryset = self.object.service_set

        return form


class DeleteSLA(DeleteView):

    model = SLA
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
