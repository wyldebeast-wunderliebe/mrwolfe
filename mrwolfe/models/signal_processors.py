from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from issue import Issue
from status import Status


@receiver(post_save, sender=Issue)
def issue_post_save(sender, instance, **kwargs):

    #send_mail('Subject here', 'Here is the message.', 'from@example.com',
    #          ['to@example.com'], fail_silently=False)
    pass

@receiver(post_save, sender=Status)
def status_post_save(sender, instance, **kwargs):

    instance.issue.status = instance.name
    instance.issue.save()
