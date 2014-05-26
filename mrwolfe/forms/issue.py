from django import forms
from mrwolfe.models.issue import Issue
from base import PartialUpdateMixin


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ("sla", "service", "title", "text", "assignee", "contact")


class IssueAssigneeForm(forms.ModelForm, PartialUpdateMixin):

    class Meta:
        model = Issue
        fields = ("assignee", )
