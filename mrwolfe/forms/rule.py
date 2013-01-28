from django import forms
from mrwolfe.models.rule import Rule


class RuleForm(forms.ModelForm):

    class Meta:
        model = Rule
        widgets = {'sla': forms.HiddenInput()}
