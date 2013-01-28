from django import forms
from mrwolfe.models.contact import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
