from django.db import models
from django.core.urlresolvers import reverse


class MailQueue(models.Model):

    usr = models.CharField(max_length=250)
    pwd = models.CharField(max_length=250)
    host = models.CharField(max_length=50)
    port = models.IntegerField(default=110, blank=True, null=True)
    protocol = models.IntegerField(
        default=0, choices=((0, "POP"), (1, "IMAP")))

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return self.usr

    def get_absolute_url(self):

        return reverse("config")
