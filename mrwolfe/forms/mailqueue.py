from django import forms
from mrwolfe.models.mailqueue import MailQueue


class MailQueueForm(forms.ModelForm):

    class Meta:
        model = MailQueue
	widgets = {'pwd': forms.PasswordInput()}
