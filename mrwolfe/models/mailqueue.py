from django.db import models


class MailQueue(models.Model):

    name = models.CharField(unique=True, max_length=100)    
    usr = models.EmailField(max_length=250)
    pwd = models.CharField(max_length=250)
    host = models.CharField(max_length=50)
    port = models.IntegerField(default=110)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return self.name
