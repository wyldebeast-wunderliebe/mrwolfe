from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView, JSONDetailView
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


class ServiceJSONSetDefault(JSONDetailView):

    model = Service
    template_name = "snippets/service.html"

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        self.object.sla.default_service = self.object
        self.object.sla.save()

        return super(ServiceJSONSetDefault, self).get(request, *args, **kwargs)
