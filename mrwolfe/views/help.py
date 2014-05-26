import os
from markdown import markdown
from django.views.generic.base import TemplateView
from django.conf import settings
from django.utils.safestring import mark_safe


class HelpView(TemplateView):

    template_name = "help.html"

    def get_context_data(self, **kwargs):
        
        ctx = super(HelpView, self).get_context_data(**kwargs)
        
        ctx.update({"view": self})
        
        return ctx    

    @property
    def help_text(self):

        """ Read the README..."""

        if self.request.path.endswith(".md"):

            doc = self.request.path.split("/")[-1]
            
            text = open(os.path.join(settings.PROJECT_ROOT, 
                                  "docs", doc)).read()
        else:
            text = open(os.path.join(settings.PROJECT_ROOT, 
                                     "docs", "intro.md")).read()

        return mark_safe(markdown(text))

