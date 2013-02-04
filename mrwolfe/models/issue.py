from datetime import datetime, timedelta
import time
from django.db import models
from user import User
from django.conf import settings
from sla import SLA
from service import Service
from contact import Contact


class Issue(models.Model):

    sla = models.ForeignKey(SLA, null=True)
    service = models.ForeignKey(Service, blank=True, null=True)
    title = models.CharField(max_length=100)
    text =  models.TextField()
    assignee = models.ForeignKey(User, blank=True, null=True,
                                 related_name="assignee_set")
    contact = models.ForeignKey(Contact, related_name="contact_set")
    status = models.CharField(
        max_length=100,
        default=settings.ISSUE_STATUS_DEFAULT,
        choices=settings.ISSUE_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    email_from = models.EmailField(blank=True, null=True)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return "%s - %s" % (self.issue_id, self.title[:50])

    @property
    def issue_id(self):
    
        return "#%08i" % self.pk

    @property
    def time_to_resolve(self):

        """ (created + hours of service) - now """
        
        now = datetime.now()

        if self.deadline:

            if self.deadline < now:

                return time.strftime("%H:%M late", 
                                     time.gmtime((now - self.deadline).seconds))
            else:
                return time.strftime("%H:%M", 
                                     time.gmtime((self.deadline - now).seconds))
        else:
            return None

    @property
    def raw_time_to_resolve(self):

        now = datetime.now()

        tts = (self.deadline - now).seconds / 3600.0

        if now > self.deadline:
            tts = -tts
            
        return tts

    @property
    def deadline(self):

        """ Deadline for this issue, or None if not applicable """

        if self.service and self.service.solution_time:
            return self.created + timedelta(hours=self.service.solution_time)
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

    @property
    def urgency(self):
        
        """ How urgent is it..? """

        tts = self.raw_time_to_resolve
        defcon = "normal"

        if tts < 1:
            defcon = "critical"
        elif tts < 2:
            defcon = "warning"

        return defcon

    @property
    def in_time(self):

        _in_time = True

        if self.deadline:
            
            compare_with = self.dateclosed or datetime.now()

            if compare_with > self.deadline:
                _in_time = False

        return _in_time
