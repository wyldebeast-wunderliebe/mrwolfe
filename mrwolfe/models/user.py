from django.db import models
from mrwolfe.models.sla import SLA
from django.contrib.auth.models import User as Base


class User(models.Model):

    """ Mr. Wolfe user """

    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField()

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        try:
            return self.contact.__unicode__()
        except:
            try:
                return self.operator.__unicode__()
            except:
                return self.email
