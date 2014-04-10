from django.views.generic.detail import DetailView


class BaseView(DetailView):

    @property
    def template_name(self):

        return "view_%s.html" % self.object.__class__.__name__.lower()

    def get_context_data(self, **kwargs):
        
        ctx = super(BaseView, self).get_context_data(**kwargs)
        
        ctx.update({"view": self})
        
        return ctx    


class CTypeMixin(object):

    @property
    def ctype(self):

        return self.model.__class__.__name__
