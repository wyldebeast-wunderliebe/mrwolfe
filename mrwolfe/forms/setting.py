from django import forms
from mrwolfe.models.setting import Setting


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ("name", "value")
