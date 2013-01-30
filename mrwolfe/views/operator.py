from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.operator import Operator
from mrwolfe.forms.operator import OperatorForm


class OperatorJSONCreate(JSONCreateView):

    model = Operator
    form_class = OperatorForm
    success_template_name = "snippets/operator.html"


class OperatorJSONEdit(JSONUpdateView):

    model = Operator
    form_class = OperatorForm
    success_template_name = "snippets/operator.html"


class OperatorJSONDelete(JSONDeleteView):

    model = Operator
