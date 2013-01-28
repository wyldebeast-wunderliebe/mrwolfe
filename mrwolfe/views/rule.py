from django import forms
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.rule import Rule
from mrwolfe.forms.rule import RuleForm


class RuleJSONCreate(JSONCreateView):

    model = Rule
    form_class = RuleForm    
    success_template_name = "snippets/rule.html"

    def get_initial(self):

        return {'sla': self.kwargs['sla_pk']}


class RuleJSONEdit(JSONUpdateView):

    model = Rule
    form_class = RuleForm    
    success_template_name = "snippets/rule.html"


class RuleJSONDelete(JSONDeleteView):

    model = Rule
