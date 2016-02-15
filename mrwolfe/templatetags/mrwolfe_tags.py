import pkg_resources
from django.template import Library
from django.conf import settings
from mrwolfe.models import Setting


register = Library()


@register.filter
def get_django_setting(name):

    """ get access to any setting in template """

    return getattr(settings, name, "")


@register.filter
def get_setting(name):

    """ Access mrwolfe setting """

    if Setting.objects.filter(name=name).exists():
        return Setting.objects.get(name=name).value
    else:
        return None


@register.inclusion_tag('snippets/css.html')
def list_plugin_css():

    css = []

    for entrypoint in pkg_resources.iter_entry_points(group="mrwolfe.skin",
                                                      name="css"):
        css.extend(entrypoint.load()())

    return {"plugin_css": css, "STATIC_URL": settings.STATIC_URL}


@register.simple_tag
def username(user):

    try:
        _name = user.username

        if user.first_name or user.last_name:
            _name = "%s %s" % (user.first_name, user.last_name)
        elif user.email:
            _name = user.email

        return _name
    except:
        pass
    return str(user)
