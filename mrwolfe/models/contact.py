from django.db import models
from mrwolfe.models.sla import SLA
from django.contrib.auth.models import User


class Contact(models.Model):

    """ Represent the customer side of things. Doesn't HAVE to be
    a vaild user """

    user = models.OneToOneField(User, null=True, blank=True)
    sla = models.ManyToManyField(SLA)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField()

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        try:
            return self.user.get_full_name()
        except:
            return self.email
