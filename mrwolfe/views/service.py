from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.service import Service
from mrwolfe.forms.service import ServiceForm


class ServiceMixin(object):

    def get_context_data(self, **kwargs):
        
        ctx = super(ServiceMixin, self).get_context_data(**kwargs)
        
        ctx.update({"view": self})
        
        return ctx


class ServiceCreate(CreateView, ServiceMixin):

    model = Service
    form_class = ServiceForm    
    template_name = "create_service.html"

    def get_initial(self):

        initial = super(CreateView, self).get_initial()

        if "sla" in self.request.GET:
            initial["sla"] = self.request.GET["sla"]

        return initial

    def get_success_url(self):

        return "/view_sla/%s?message=Service+aangemaakt&status=0" % \
            self.object.sla.pk


class ServiceJSONCreate(JSONCreateView, ServiceMixin):

    model = Service
    form_class = ServiceForm    
    success_template_name = "snippets/service.html"

    def get_initial(self):

        return {'sla': self.kwargs['sla_pk']}

    def get_form(self, form_class):
        
        form = super(ServiceJSONCreate, self).get_form(form_class)

        form.fields['sla'].widget = forms.HiddenInput()

        return form


class ServiceEdit(UpdateView, ServiceMixin):

    model = Service
    form_class = ServiceForm    
    template_name = "edit_service.html"

    def get_success_url(self):

        return "/?message=Service+gewijzigd&status=0"


class ServiceJSONEdit(JSONUpdateView, ServiceMixin):

    model = Service
    form_class = ServiceForm    
    success_template_name = "snippets/service.html"


class ServiceDelete(DeleteView, ServiceMixin):

    model = Service

    def get_success_url(self):

        return "/?message=Service+verwijderd&status=0"


class ServiceJSONDelete(JSONDeleteView, ServiceMixin):

    model = Service
