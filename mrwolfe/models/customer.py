from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        app_label = "mrwolfe"
        ordering = ["name"]

    def __unicode__(self):
        return self.name
