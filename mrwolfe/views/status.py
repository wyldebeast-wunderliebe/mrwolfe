from django.views.generic.edit import UpdateView
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from mrwolfe.models.issue import Issue
from mrwolfe.forms.status import StatusForm


class CreateStatus(UpdateView):

    model = Issue
    form_class = StatusForm
    template_name = "create_status.html"

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():

            self.object.status_history.create(
                name=form.cleaned_data['name'],
                comment=form.cleaned_data['comment']
            )

            self.object.status = form.cleaned_data['name']

            self.object.save()

        return HttpResponse(render_to_string(
            'controls/status_control.html',
            {'view': self, 'object': self.object,
             'redir': self.object.is_closed}
        ))

    @property
    def status_name(self):

        return self.request.GET.get('status', '')

    def get_initial(self):

        return {'name': self.status_name}

    def list_status_options(self):

        return (opt for opt in settings.ISSUE_STATUS_CHOICES
                if opt[0] != self.status_name)
