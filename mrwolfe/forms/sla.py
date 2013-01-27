from django import forms
from mrwolfe.models.sla import SLA


class SLAForm(forms.ModelForm):

    class Meta:
        model = SLA
