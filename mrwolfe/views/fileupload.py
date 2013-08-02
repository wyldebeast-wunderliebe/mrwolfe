import json
import os
from tempfile import mkstemp
import uuid
from shutil import copyfile
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.files.base import ContentFile
import logging as log
import mimetypes
from django.conf import settings
from django.core.files import File
from mrwolfe.models import Attachment, Issue


class UploadView(View):

    """ View that enables Ajax style upload of attachments """

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        issue = Issue.objects.get(pk=request.POST["issue_id"])

        temp_file = None
        file_name = None

        for filename in request.FILES.keys():

            fd, temp_file = self.create_temp_file(request.FILES[filename])
            file_name = request.FILES[filename].name
            mime_type = request.FILES[filename].content_type or \
                mimetypes.guess_type(file_name)[0]

            att = Attachment()
            att._file = ContentFile(open(temp_file).read())
            att._file.name = file_name
            att.mimetype = mime_type
            att.issue = issue
            att.save()

        # Send back results to the client. Client should 'handle'
        # file_id etc.
        #
        context = {}

        attachments = issue.attachment_set.all()

        template = "snippets/attachments.html"

        context['html'] = render_to_string(template, 
                                           {'attachments': attachments})

        response = HttpResponse(json.dumps(context), content_type="text/plain")

        return response

    def create_temp_file(self, data):

        fd, path = mkstemp()

        block = data.read(1024)
        while block:
            os.write(fd, block)
            block = data.read(1024)

        os.close(fd)
        return fd, path
