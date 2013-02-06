from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.views.generic import FormView
from mrwolfe.forms.login import LoginForm


class LoginView(FormView):

    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def get(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)
        
        return self.render_to_response(self.get_context_data(form=form, **kwargs))        

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.form_class)

        if not form.is_valid():

            return self.get(request, *args, **kwargs)

        user = authenticate(username=form.cleaned_data["username"],
                            password=form.cleaned_data["password"])

        if not user:
            return self.get(request, *args, **kwargs)
        
        # Persist user
        #
        login(request, user)
        
        return HttpResponseRedirect(self.get_success_url())
