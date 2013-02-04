from django.db import models
from django.contrib.auth.models import User as BaseUser
from user import User


class Operator(User):

    user = models.OneToOneField(BaseUser)

    class Meta:
        app_label = "mrwolfe"

    def __unicode__(self):
        
        return self.user.get_full_name() or self.email
