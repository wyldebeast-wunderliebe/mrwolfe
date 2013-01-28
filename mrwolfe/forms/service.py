from django import forms
from mrwolfe.models.service import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        widgets = {'sla': forms.HiddenInput()}
