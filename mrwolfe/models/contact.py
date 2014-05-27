from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.core.urlresolvers import reverse
from mrwolfe.models.sla import SLA
from user import User


class Contact(User):

    """ Represent the customer side of things. Doesn't HAVE to be
    a valid user for Django """

    user = models.OneToOneField(BaseUser, null=True, blank=True)
    sla = models.ManyToManyField(SLA, null=True, blank=True)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        try:
            return self.user.get_full_name() or self.email
        except:
            return self.email

    def get_absolute_url(self):

        return reverse("config")
