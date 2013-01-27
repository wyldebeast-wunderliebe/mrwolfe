from django.db import models
from customer import Customer
from mailqueue import MailQueue


class SLA(models.Model):

    name = models.CharField(unique=True, max_length=100)    
    customer = models.ForeignKey(Customer)
    start_date = models.DateField()
    end_date = models.DateField()
    mailqueue = models.ForeignKey(MailQueue)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        return "%s (%s, %s / %s)" % (self.name, self.customer, self.start_date,
                                    self.end_date)

    def is_contact(self, contact):

        """ Is the given contact a valid contact for this sla? """
        
        return contact.customer == self.customer
