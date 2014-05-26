from django.db import models
from issue import Issue


class Comment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issue, related_name="comments")
    comment = models.TextField()

    class Meta:
        app_label = "mrwolfe"
        ordering = ["date"]

    def __unicode__(self):
        return self.comment[:50]
