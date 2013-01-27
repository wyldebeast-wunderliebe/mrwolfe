from django import forms
from mrwolfe.models.operator import Operator


class OperatorForm(forms.ModelForm):

    class Meta:
        model = Operator
