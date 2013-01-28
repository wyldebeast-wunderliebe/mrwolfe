from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.service import Service
from mrwolfe.forms.service import ServiceForm


class ServiceJSONCreate(JSONCreateView):

    model = Service
    form_class = ServiceForm    
    success_template_name = "snippets/service.html"

    def get_initial(self):

        return {'sla': self.kwargs['sla_pk']}


class ServiceJSONEdit(JSONUpdateView):

    model = Service
    form_class = ServiceForm    
    success_template_name = "snippets/service.html"


class ServiceJSONDelete(JSONDeleteView):

    model = Service
