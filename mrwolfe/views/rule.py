from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.rule import Rule
from mrwolfe.forms.rule import RuleForm
from base import CTypeMixin


class CreateRule(CreateView, CTypeMixin):

    model = Rule
    form_class = RuleForm    
    template_name = "addform.html"

    def get_initial(self):

        return {'sla': self.kwargs['sla_pk']}


class UpdateRule(UpdateView):

    model = Rule
    form_class = RuleForm    
    template_name = "editform.html"


class DeleteRule(DeleteView):

    model = Rule
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
