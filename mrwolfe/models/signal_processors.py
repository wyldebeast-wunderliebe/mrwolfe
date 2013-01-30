from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from issue import Issue
from status import Status
from mrwolfe.notification import notify


@receiver(post_save, sender=Issue)
def issue_post_save(sender, instance, **kwargs):

    pass

@receiver(post_save, sender=Status)
def status_post_save(sender, instance, **kwargs):

    instance.issue.status = instance.name
    instance.issue.save()

    if instance.name == settings.ISSUE_STATUS_CLOSED:

        notify("issue_closed", 
               {"issue": instance.issue, "comment": instance.comment},
               settings.DEFAULT_FROM_ADDR, 
               instance.issue.contact.email)
        
