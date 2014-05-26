from django import forms
from mrwolfe.models.comment import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {'issue': forms.HiddenInput()}
