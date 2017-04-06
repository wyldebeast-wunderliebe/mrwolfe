from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.core.urlresolvers import reverse
from .user import User


class Operator(User):

    user = models.OneToOneField(BaseUser)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return self.user.get_full_name() or self.email

    def get_absolute_url(self):

        return reverse("config")
