from django.db import models
from mailqueue import MailQueue


class SLA(models.Model):

    name = models.CharField(unique=True, max_length=100)    
    start_date = models.DateField()
    end_date = models.DateField()
    default_service = models.ForeignKey("Service", null=True, blank=True,
                                        related_name="defaultservice")

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return "%s (%s / %s)" % (self.name, 
                                 self.start_date.strftime("%d-%m-%Y"),
                                 self.end_date.strftime("%d-%m-%Y"))

    def is_contact(self, contact):

        """ Is the given contact a valid contact for this sla? """
        
        return self.contact_set.filter(pk=contact.pk).exists()
