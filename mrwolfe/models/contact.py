from django.db import models
from mrwolfe.models.customer import Customer
from django.contrib.auth.models import User


class Contact(models.Model):

    user = models.OneToOneField(User)
    customer = models.ForeignKey(Customer)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        app_label = "mrwolfe"
