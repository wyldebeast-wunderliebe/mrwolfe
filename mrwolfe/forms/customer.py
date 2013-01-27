from django import forms
from mrwolfe.models.customer import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
