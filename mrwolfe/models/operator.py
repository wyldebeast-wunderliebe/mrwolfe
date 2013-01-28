from django.db import models
from django.contrib.auth.models import User


class Operator(models.Model):

    user = models.OneToOneField(User)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        
        return self.user.get_full_name()
