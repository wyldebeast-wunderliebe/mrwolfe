from django.db import models


class Setting(models.Model):

    """ Poor man's utility """

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return "%s: %s" % (self.name, self.value)
