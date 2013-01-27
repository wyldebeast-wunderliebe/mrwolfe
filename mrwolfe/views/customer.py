from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mrwolfe.models.customer import Customer
from mrwolfe.forms.customer import CustomerForm


class CustomerCreate(CreateView):

    model = Customer
    form_class = CustomerForm
    template_name = "create_customer.html"

    def get_success_url(self):

        return "/?message=Customer+aangemaakt&status=0"


class CustomerEdit(UpdateView):

    model = Customer
    form_class = CustomerForm
    template_name = "edit_customer.html"

    def get_success_url(self):

        return "/?message=Customer+gewijzigd&status=0"


class CustomerDelete(DeleteView):

    model = Customer

    def get_success_url(self):

        return "/?message=Customer+Verwijderd&status=0"
