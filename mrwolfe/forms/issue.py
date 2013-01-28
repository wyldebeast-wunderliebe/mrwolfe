from django import forms
from mrwolfe.models.issue import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ("sla", "service", "title", "text", "assignee", "contact")
