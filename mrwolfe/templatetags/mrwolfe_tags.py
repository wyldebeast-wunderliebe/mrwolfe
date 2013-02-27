import pkg_resources
from django.template import Library
from django.conf import settings


register = Library()


@register.inclusion_tag('snippets/css.html')
def list_plugin_css():

    css = []

    for entrypoint in pkg_resources.iter_entry_points(group="mrwolfe.skin",
                                                      name="css"):        
        css.extend(entrypoint.load()())

    return {"plugin_css": css, "STATIC_URL": settings.STATIC_URL}
