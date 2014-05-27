from django.db import models
from django.conf import settings
from issue import Issue


class Status(models.Model):

    name = models.CharField(max_length=100,
                            choices=settings.ISSUE_STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, related_name="status_history")
    comment = models.TextField(null=True, blank=True)

    class Meta:
        app_label = "mrwolfe"
        ordering = ["-date"]

    def __unicode__(self):
        return self.name
