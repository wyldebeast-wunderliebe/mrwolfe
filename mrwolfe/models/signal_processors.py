from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from issue import Issue
from comment import Comment
from status import Status
from operator import Operator
from mrwolfe.notification import notify


@receiver(post_save, sender=Issue)
def issue_post_save(sender, instance, **kwargs):

    operators = [op.email for op in Operator.objects.all()]

    notify("issue_created", 
           {"issue": instance},
           settings.DEFAULT_FROM_ADDR,
           ", ".join(operators))


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, **kwargs):

    notify("comment_added", 
           {"issue": instance.issue, "comment": instance},
           settings.DEFAULT_FROM_ADDR,
           instance.issue.contact.email
           )

@receiver(post_save, sender=Status)
def status_post_save(sender, instance, **kwargs):

    instance.issue.status = instance.name
    instance.issue.save()

    if instance.name == settings.ISSUE_STATUS_CLOSED:

        notify("issue_closed", 
               {"issue": instance.issue, "comment": instance.comment},
               instance.issue.email_from or settings.DEFAULT_FROM_ADDR,
               instance.issue.contact.email)        
    else:
        notify("issue_status", 
               {"issue": instance.issue, "comment": instance.comment},
               instance.issue.email_from or settings.DEFAULT_FROM_ADDR,
               instance.issue.contact.email)
