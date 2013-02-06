from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.comment import Comment
from mrwolfe.forms.comment import CommentForm


class CommentJSONCreate(JSONCreateView):

    model = Comment
    form_class = CommentForm
    success_template_name = "snippets/comment.html"

    def get_initial(self):

        return {'issue': self.kwargs['issue_pk']}

class CommentJSONEdit(JSONUpdateView):

    model = Comment
    form_class = CommentForm
    success_template_name = "snippets/comment.html"


class CommentJSONDelete(JSONDeleteView):

    model = Comment
