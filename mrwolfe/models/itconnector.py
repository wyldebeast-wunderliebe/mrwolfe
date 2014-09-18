from django.db import models
from django.core.urlresolvers import reverse


class ITConnector(models.Model):

    """ Represent a connector instance to an Issue Tracking system """

    name = models.CharField(max_length=250, unique=True)
    connector_type = models.CharField(max_length=50)
    usr = models.CharField(max_length=250)
    pwd = models.CharField(max_length=250)
    uri = models.CharField(max_length=50)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return self.name

    def get_absolute_url(self):

        return reverse("config")
