from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.operator import Operator
from mrwolfe.forms.operator import OperatorForm
from base import CTypeMixin


class CreateOperator(CreateView, CTypeMixin):

    model = Operator
    form_class = OperatorForm
    template_name = "addform.html"


class UpdateOperator(UpdateView):

    model = Operator
    form_class = OperatorForm
    template_name = "editform.html"


class DeleteOperator(DeleteView):

    model = Operator
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
