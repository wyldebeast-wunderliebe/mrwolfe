from django.views.generic.edit import UpdateView
from mrwolfe.models import Setting
from mrwolfe.forms.setting import SettingForm


class UpdateSetting(UpdateView):

    model = Setting
    form_class = SettingForm
    template_name = "snippets/setting.html"

    def get_object(self, queryset=None):

        return Setting.objects.get(name=self.request.GET['name'])

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        if self.request.GET.get('value'):

            self.object.value = self.request.GET.get('value')
            self.object.save()

        return super(UpdateSetting, self).get(request, *args, **kwargs)
