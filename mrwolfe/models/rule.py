import re
from django.db import models
from django.conf import settings
from mrwolfe.models.sla import SLA


class Rule(models.Model):

    """ SLA matching rule for email messages """

    sla = models.ForeignKey(SLA)
    field = models.CharField(choices=settings.MESSAGE_FIELDS, max_length=100)
    regexp = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):

        return "%s matches %s" % (self.field, self.regexp)

    def matches(self, message):

        """ Message should be a email.Message object """

        try:
            if self.field != "text":
                return re.search(self.regexp, message[self.field])
            else:
                return re.search(self.regexp, message.as_string())
        except:
            return False
