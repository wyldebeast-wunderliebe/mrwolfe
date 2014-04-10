from django.db import models
from sla import SLA
from django.core.urlresolvers import reverse


class Service(models.Model):

    sla = models.ForeignKey(SLA)
    response_time = models.FloatField(null=True)
    solution_time = models.FloatField(null=True)
    priority = models.CharField(max_length=100)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return "%s: respond < %s hours, resolve < %s hours" % \
            (self.priority, self.response_time, self.solution_time)

    @property
    def is_default(self):

        return self == self.sla.default_service

    def get_absolute_url(self):

        return reverse("config")
