from django import forms
from mrwolfe.models.status import Status


class StatusForm(forms.ModelForm):

    no_comment = forms.BooleanField("No comment")
    no_notification = forms.BooleanField("Do not send notification")

    class Meta:
        model = Status
        fields = ('comment', 'no_comment', 'no_notification', 'name', 'issue')
        widgets = {'issue': forms.HiddenInput(), 'name': forms.HiddenInput()}
