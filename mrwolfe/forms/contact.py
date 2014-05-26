from django import forms
from mrwolfe.models.contact import Contact


class ContactForm(forms.ModelForm):

    labels = {"cancel": "Cancel", "submit": "Save"}

    class Meta:
        model = Contact
