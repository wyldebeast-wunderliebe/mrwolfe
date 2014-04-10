from django.views.generic.edit import CreateView
from mrwolfe.models.comment import Comment
from mrwolfe.forms.comment import CommentForm


class CreateComment(CreateView):

    model = Comment
    form_class = CommentForm
    template_name = "snippets/comment.html"

    def form_valid(self, form):

        form.instance.save()

        return self.render_to_response({'object': form.instance})
