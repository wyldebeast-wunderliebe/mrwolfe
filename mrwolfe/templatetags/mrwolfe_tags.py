import pkg_resources
from django.template import Library
from django.conf import settings


register = Library()


@register.filter
def get_setting(name):

    """ get access to any setting in template """

    return getattr(settings, name, "")


@register.inclusion_tag('snippets/css.html')
def list_plugin_css():

    css = []

    for entrypoint in pkg_resources.iter_entry_points(group="mrwolfe.skin",
                                                      name="css"):
        css.extend(entrypoint.load()())

    return {"plugin_css": css, "STATIC_URL": settings.STATIC_URL}


@register.simple_tag
def username(user):

    _name = user.username

    if user.first_name or user.last_name:
        _name = "%s %s" % (user.first_name, user.last_name)
    elif user.email:
        _name = user.email

    return _name
