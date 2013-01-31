from django.db import models
from mrwolfe.models.sla import SLA
from django.contrib.auth.models import User as BaseUser
from user import User


class Contact(User):

    """ Represent the customer side of things. Doesn't HAVE to be
    a valid user for Django """

    user = models.OneToOneField(BaseUser, null=True, blank=True)
    sla = models.ManyToManyField(SLA)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        try:
            return self.user.get_full_name()
        except:
            return self.email
