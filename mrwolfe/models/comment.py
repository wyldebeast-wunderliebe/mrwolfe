from django.db import models
from issue import Issue
from mrwolfe.models.user import User


class Comment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, related_name="comments")
    comment = models.TextField()
    comment_by = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        app_label = "mrwolfe"
        ordering = ["date"]

    def __unicode__(self):
        return self.comment[:50]
