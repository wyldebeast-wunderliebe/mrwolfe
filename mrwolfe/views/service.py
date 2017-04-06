from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.service import Service
from mrwolfe.forms.service import ServiceForm
from .base import CTypeMixin


class CreateService(CreateView, CTypeMixin):

    model = Service
    form_class = ServiceForm
    template_name = "addform.html"

    def get_initial(self):

        return {'sla': self.kwargs['sla_pk']}


class UpdateService(UpdateView, CTypeMixin):

    model = Service
    form_class = ServiceForm
    template_name = "editform.html"


class DeleteService(DeleteView):

    model = Service
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")


class ServiceSetDefault(UpdateView):

    model = Service
    form_class = ServiceForm
    template_name = "snippets/service.html"

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        self.object.sla.default_service = self.object
        self.object.sla.save()

        return super(ServiceSetDefault, self).get(request, *args, **kwargs)
