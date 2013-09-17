from django.db import models


class MailQueue(models.Model):

    usr = models.EmailField(max_length=250, unique=True)
    pwd = models.CharField(max_length=250)
    host = models.CharField(max_length=50)
    port = models.IntegerField(default=110, blank=True, null=True)
    protocol = models.IntegerField(default=0, choices=((0, "POP"), (1, "IMAP")))

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return self.usr
