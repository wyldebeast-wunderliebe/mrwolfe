from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pu_in_content.views.jsonbase import JSONCreateView, JSONUpdateView, \
    JSONDeleteView
from mrwolfe.models.customer import Customer
from mrwolfe.forms.customer import CustomerForm


class CustomerCreate(CreateView):

    model = Customer
    form_class = CustomerForm
    template_name = "create_customer.html"

    def get_success_url(self):

        return "/?message=Customer+aangemaakt&status=0"


class CustomerJSONCreate(JSONCreateView):

    model = Customer
    form_class = CustomerForm    
    success_template_name = "snippets/customer.html"


class CustomerEdit(UpdateView):

    model = Customer
    form_class = CustomerForm
    template_name = "edit_customer.html"

    def get_success_url(self):

        return "/?message=Customer+gewijzigd&status=0"


class CustomerJSONEdit(JSONUpdateView):

    model = Customer
    form_class = CustomerForm
    success_template_name = "edit_customer.html"


class CustomerDelete(DeleteView):

    model = Customer

    def get_success_url(self):

        return "/?message=Customer+Verwijderd&status=0"


class CustomerJSONDelete(JSONDeleteView):

    model = Customer
