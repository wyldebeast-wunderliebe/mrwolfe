from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.forms.mailqueue import MailQueueForm
from base import CTypeMixin


class CreateMailQueue(CreateView, CTypeMixin):

    model = MailQueue
    form_class = MailQueueForm
    template_name = "addform.html"


class UpdateMailQueue(UpdateView, CTypeMixin):

    model = MailQueue
    form_class = MailQueueForm
    template_name = "editform.html"


class DeleteMailQueue(DeleteView):

    model = MailQueue
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
