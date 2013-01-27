from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.forms.mailqueue import MailQueueForm


class MailQueueCreate(CreateView):

    model = MailQueue
    form_class = MailQueueForm
    template_name = "create_mailqueue.html"

    def get_success_url(self):

        return "/?message=MailQueue+aangemaakt&status=0"


class MailQueueEdit(UpdateView):

    model = MailQueue
    form_class = MailQueueForm
    template_name = "edit_mailqueue.html"

    def get_success_url(self):

        return "/?message=MailQueue+gewijzigd&status=0"


class MailQueueDelete(DeleteView):

    model = MailQueue

    def get_success_url(self):

        return "/?message=MailQueue+verwijderd&status=0"
