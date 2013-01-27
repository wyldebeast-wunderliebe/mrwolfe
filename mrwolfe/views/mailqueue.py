from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.forms.mailqueue import MailQueueForm


class MailQueueJSONCreate(JSONCreateView):

    model = MailQueue
    form_class = MailQueueForm
    success_template_name = "snippets/mailqueue.html"


class MailQueueJSONEdit(JSONUpdateView):

    model = MailQueue
    form_class = MailQueueForm
    success_template_name = "snippets/mailqueue.html"


class MailQueueJSONDelete(JSONDeleteView):

    model = MailQueue
