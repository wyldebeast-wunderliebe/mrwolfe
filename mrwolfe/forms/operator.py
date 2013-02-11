from django import forms
from mrwolfe.models.operator import Operator


class OperatorForm(forms.ModelForm):

    labels = {"cancel": "Cancel", "submit": "Save"}

    class Meta:
        model = Operator
