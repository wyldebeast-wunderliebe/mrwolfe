import os
from django.db import models
from django.conf import settings
from issue import Issue


class Attachment(models.Model):

    issue = models.ForeignKey(Issue)
    _file = models.FileField('Attachment', upload_to="attachments/%Y/%m/%d")
    mimetype = models.CharField(max_length=50)

    class Meta:
        app_label = "mrwolfe"

    @property
    def filename(self):
        return os.path.split(self._file.name)[1]

    @property
    def is_image(self):
        return "image" in self.mimetype

    @property
    def download_url(self):

        return os.path.join(settings.MEDIA_URL, self._file.name)

    @property
    def icon(self):

        return "file"

    @property
    def filesize(self):

        def sizeof_fmt(num):
            for x in ['bytes','KB','MB','GB','TB']:
                if num < 1024.0:
                    return "%3.1f %s" % (num, x)
                num /= 1024.0

        return sizeof_fmt(self._file.size)
