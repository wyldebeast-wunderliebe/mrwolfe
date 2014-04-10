from django import forms
from mrwolfe.models.status import Status


class StatusForm(forms.ModelForm):

    skip_notification = forms.BooleanField(
        label="Skip notification",
        required=False
    )

    class Meta:
        model = Status
        fields = ('comment', 'name', 'skip_notification')
        widgets = {'name': forms.HiddenInput()}
