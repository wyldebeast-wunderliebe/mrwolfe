from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.contact import Contact
from mrwolfe.forms.contact import ContactForm


class ContactJSONCreate(JSONCreateView):

    model = Contact
    form_class = ContactForm
    success_template_name = "snippets/contact.html"


class ContactJSONEdit(JSONUpdateView):

    model = Contact
    form_class = ContactForm
    success_template_name = "snippets/contact.html"


class ContactJSONDelete(JSONDeleteView):

    model = Contact
