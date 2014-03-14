from django import forms
from mrwolfe.models.status import Status


class StatusForm(forms.ModelForm):

    no_comment = forms.BooleanField("No comment", required=False)
    no_notification = forms.BooleanField("Do not send notification",
                                         required=False)

    class Meta:
        model = Status
        fields = ('comment', 'no_comment', 'no_notification', 'name', 'issue')
        widgets = {'issue': forms.HiddenInput(), 'name': forms.HiddenInput()}
