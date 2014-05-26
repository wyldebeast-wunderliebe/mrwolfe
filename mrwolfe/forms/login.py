from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):

    username = forms.CharField(label=_("Username"),
                               max_length=30, widget=forms.TextInput())
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(render_value=False))
