from django import forms
from mrwolfe.models.issue import Issue
from .base import PartialUpdateMixin


class IssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(IssueForm, self).__init__(*args, **kwargs)

        try:
            services = self.instance.sla.service_set.all()

            self.fields['service'].widget.choices = self._service_vocab(
                services)
        except:
            pass

    def _service_vocab(self, services):

        return tuple([('', '---------')] +
                     [(service.id, unicode(service)) for service in services])

    class Meta:
        model = Issue
        fields = ("sla", "service", "title", "text", "assignee", "contact")


class IssueAssigneeForm(forms.ModelForm, PartialUpdateMixin):
    class Meta:
        model = Issue
        fields = ("assignee", )
