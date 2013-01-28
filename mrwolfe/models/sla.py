from django.db import models
from mailqueue import MailQueue


class SLA(models.Model):

    name = models.CharField(unique=True, max_length=100)    
    start_date = models.DateField()
    end_date = models.DateField()
    mailqueue = models.ForeignKey(MailQueue)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return "%s (%s / %s)" % (self.name, self.start_date, self.end_date)

    def is_contact(self, contact):

        """ Is the given contact a valid contact for this sla? """
        
        return self.contact_set.filter(pk=contact.pk).exists()
