from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from mrwolfe.models.comment import Comment
from mrwolfe.forms.comment import CommentForm


class CreateComment(CreateView):

    model = Comment
    form_class = CommentForm
    template_name = "snippets/comment.html"

    def get_success_url(self):
        return reverse("view_issue", kwargs={'pk':self.object.issue.id})

    def form_valid(self, form):

        if self.request.user.operator:
            form.instance.comment_by = self.request.user.operator
        elif self.request.user.contact:
            form.instance.comment_by = self.request.user.contact

        form.instance.save()

        return super(CreateComment, self).form_valid(form)
