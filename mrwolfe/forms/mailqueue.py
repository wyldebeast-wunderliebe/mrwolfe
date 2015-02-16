from django import forms
from mrwolfe.models.mailqueue import MailQueue


class MailQueueForm(forms.ModelForm):
    labels = {"cancel": "Cancel", "submit": "Save"}

    class Meta:
        model = MailQueue
        widgets = {'pwd': forms.PasswordInput()}
        fields = ("usr", "pwd", "host", "port", "protocol")
