from django.db import models
from sla import SLA


class Service(models.Model):

    sla = models.ForeignKey(SLA)
    response_time = models.FloatField(null=True)
    solution_time = models.FloatField(null=True)
    priority = models.CharField(max_length=100)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return "%s: %s hours" % (self.priority, self.response_time)
