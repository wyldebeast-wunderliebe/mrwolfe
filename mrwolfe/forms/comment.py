from django import forms
from mrwolfe.models.comment import Comment


class CommentForm(forms.ModelForm):

    #no_notification = forms.BooleanField("Do not send notification",
    #                                     required=False)

    class Meta:
        model = Comment
        widgets = {'issue': forms.HiddenInput()}
