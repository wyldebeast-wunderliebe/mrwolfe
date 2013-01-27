from django import forms
from mrwolfe.models.status import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('comment', 'name', 'issue')
        widgets = {'issue': forms.HiddenInput(), 'name': forms.HiddenInput()}
