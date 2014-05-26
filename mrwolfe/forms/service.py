from django import forms
from mrwolfe.models.service import Service


class ServiceForm(forms.ModelForm):

    @property
    def help(self):

        return self._meta.model.__doc__ or ""

    class Meta:
        model = Service
        widgets = {'sla': forms.HiddenInput()}
