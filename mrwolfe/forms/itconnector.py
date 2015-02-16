from django import forms
from mrwolfe.models.itconnector import ITConnector
from mrwolfe.itconn.base import ITCRegistry


class ITConnectorForm(forms.ModelForm):
    labels = {"cancel": "Cancel", "submit": "Save"}

    def __init__(self, *args, **kwargs):
        super(ITConnectorForm, self).__init__(*args, **kwargs)

        self.fields['connector_type'].widget.choices = self._type_choices()

    def _type_choices(self):
        return [(key, ITCRegistry.get_attr(key, 'label', key))
                for key in ITCRegistry.list_types()]

    class Meta:
        model = ITConnector
        widgets = {'pwd': forms.PasswordInput(),
                   'connector_type': forms.Select()}
        fields = ("name", "connector_type", "usr", "pwd", "uri")
