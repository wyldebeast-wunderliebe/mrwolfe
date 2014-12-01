from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from issue import Issue
from comment import Comment
from status import Status
from operator import Operator
from mrwolfe.notification import notify


@receiver(post_save, sender=Issue)
def issue_post_save(sender, instance, created=False, **kwargs):

    if created:

        operators = [op.email for op in Operator.objects.all()]

        if operators:

            notify("issue_created",
                   {"issue": instance},
                   settings.DEFAULT_FROM_ADDR,
                   ", ".join(operators))


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created=False, **kwargs):

    # who should receive notification of this comment?
    # - the issue's contact
    # - the issue assignee if the issue has one
    # - if issue has no assignee, all operators

    send_to = [instance.issue.contact.email, ]

    if instance.issue.assignee:
        send_to.append(instance.issue.assignee.email)
    else:
        operators = [op.email for op in Operator.objects.all()]
        send_to.append(operators)

    to_addr = ", ".join(to)

    if created:

        notify("comment_added",
               {"issue": instance.issue, "comment": instance},
               settings.DEFAULT_FROM_ADDR,
               to_addr,
               )

    # trigger save on issue, to reindex
    instance.issue.save()


@receiver(post_save, sender=Status)
def status_post_save(sender, instance, created=False, **kwargs):

    if not created:
        return

    instance.issue.status = instance.name
    instance.issue.save()

    if instance.name == settings.ISSUE_STATUS_CLOSED:

        notify("issue_closed",
               {"issue": instance.issue, "comment": instance.comment},
               instance.issue.email_from,
               instance.issue.contact.email)
    else:
        notify("issue_status",
               {"issue": instance.issue, "comment": instance.comment},
               instance.issue.email_from,
               instance.issue.contact.email)
