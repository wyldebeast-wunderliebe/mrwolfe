from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.itconnector import ITConnector
from mrwolfe.forms.itconnector import ITConnectorForm
from base import CTypeMixin


class CreateITConnector(CreateView, CTypeMixin):

    model = ITConnector
    form_class = ITConnectorForm
    template_name = "addform.html"


class UpdateITConnector(UpdateView, CTypeMixin):

    model = ITConnector
    form_class = ITConnectorForm
    template_name = "editform.html"


class DeleteITConnector(DeleteView):

    model = ITConnector
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
