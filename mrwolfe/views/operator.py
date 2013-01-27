from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mrwolfe.models.operator import Operator
from mrwolfe.forms.operator import OperatorForm


class OperatorCreate(CreateView):

    model = Operator
    form_class = OperatorForm
    template_name = "create_operator.html"

    def get_success_url(self):

        return "/?message=Operator+aangemaakt&status=0"


class OperatorEdit(UpdateView):

    model = Operator
    form_class = OperatorForm
    template_name = "edit_operator.html"

    def get_success_url(self):

        return "/?message=Operator+gewijzigd&status=0"


class OperatorDelete(DeleteView):

    model = Operator

    def get_success_url(self):

        return "/?message=Operator+Verwijderd&status=0"
