from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mrwolfe.models.issue import Issue
from mrwolfe.models.itconnector import ITConnector
from django.conf import settings


class ScheduleIssue(UpdateView):

    model = Issue

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        connector = ITConnector.objects.get(pk=request.GET.get("itc"))

        connector.create_issue(self.object)

        self.object.status = settings.ISSUE_STATUS_SCHEDULED

        self.object.save()

        return HttpResponseRedirect(reverse("view_issue",
                                            kwargs={'pk': self.object.pk}))
