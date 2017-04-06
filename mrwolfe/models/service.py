from django.db import models
from .sla import SLA
from django.core.urlresolvers import reverse


class Service(models.Model):

    """Service for a given SLA. This is a combination of a priority, and
    a response/resolution time. Response times are usually as per
    contract, resolution times are often used to specify an average,
    as no guarantee can be given to an actual resolution per issue.
    """

    sla = models.ForeignKey(SLA)
    response_time = models.FloatField(
        null=True,
        help_text="Response time in hours. Use '.' for decimals. Note that"
        "2.5 means two and a half hours, not two hours and 50 minutes."
    )
    solution_time = models.FloatField(
        null=True,
        help_text="Time to resolve in hours. Same behavior as response time."
    )
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
