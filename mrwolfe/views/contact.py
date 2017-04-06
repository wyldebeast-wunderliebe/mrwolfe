from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mrwolfe.models.contact import Contact
from mrwolfe.forms.contact import ContactForm
from .base import CTypeMixin


class CreateContact(CreateView, CTypeMixin):

    model = Contact
    form_class = ContactForm
    template_name = "addform.html"


class UpdateContact(UpdateView, CTypeMixin):

    model = Contact
    form_class = ContactForm
    template_name = "editform.html"


class DeleteContact(DeleteView):

    model = Contact
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("config")
