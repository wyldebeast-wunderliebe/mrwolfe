from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.operator import Operator
from mrwolfe.forms.operator import OperatorForm


class OperatorCreate(CreateView):

    model = Operator
    form_class = OperatorForm
    template_name = "create_operator.html"

    def get_success_url(self):

        return "/?message=Operator+aangemaakt&status=0"


class OperatorJSONCreate(JSONCreateView):

    model = Operator
    form_class = OperatorForm
    success_template_name = "snippets/operator.html"


class OperatorEdit(UpdateView):

    model = Operator
    form_class = OperatorForm
    template_name = "edit_operator.html"

    def get_success_url(self):

        return "/?message=Operator+gewijzigd&status=0"


class OperatorJSONEdit(JSONUpdateView):

    model = Operator
    form_class = OperatorForm
    success_template_name = "snippets/operator.html"


class OperatorDelete(DeleteView):

    model = Operator

    def get_success_url(self):

        return "/?message=Operator+Verwijderd&status=0"


class OperatorJSONDelete(JSONDeleteView):

    model = Operator
