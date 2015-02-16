from django import forms
from mrwolfe.models.sla import SLA


class SLAForm(forms.ModelForm):
    labels = {"cancel": "Cancel", "submit": "Save"}

    class Meta:
        model = SLA
        fields = ("name", "start_date", "end_date", "default_service", "email_from")
        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={'class': 'date'},
                format="%d-%m-%Y"),
            'end_date': forms.DateTimeInput(
                attrs={'class': 'date'},
                format="%d-%m-%Y"
            )}
