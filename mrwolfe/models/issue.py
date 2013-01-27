from datetime import datetime, timedelta
import time
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from sla import SLA
from service import Service


class Issue(models.Model):

    sla = models.ForeignKey(SLA, null=True)
    priority = models.ForeignKey(Service, blank=True, null=True)
    title = models.CharField(max_length=100)
    text =  models.TextField()
    assignee = models.ForeignKey(User, blank=True, null=True,
                                 related_name="assignee_set")
    contact = models.ForeignKey(User, related_name="contact_set")
    status = models.CharField(
        max_length=100,
        default=settings.ISSUE_STATUS_DEFAULT,
        choices=settings.ISSUE_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return "%s - %s - %s" % (self.status, self.created, self.text[:50])

    @property
    def issue_id(self):
    
        return "#%08i" % self.pk

    @property
    def time_to_resolve(self):

        """ (created + hours of service) - now """
        
        if self.deadline:
            return time.strftime("%H:%M", 
                                 time.gmtime((self.deadline - \
                                                  datetime.now()).seconds))
        else:
            return None

    @property
    def deadline(self):

        """ Deadline for this issue, or None if not applicable """

        if self.priority:
            return self.created + timedelta(hours=self.priority.response_time)
        else:
            return None

    def is_open(self):

        return self.status == settings.ISSUE_STATUS_OPEN

    @property
    def dateclosed(self):
        
        if self.status == settings.ISSUE_STATUS_CLOSED:
            return self.status_history.filter(
                name=settings.ISSUE_STATUS_CLOSED)[0].date
        else:
            return None
