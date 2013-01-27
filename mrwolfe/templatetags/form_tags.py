from django.template import Library
from django.core.urlresolvers import reverse


register = Library()


@register.inclusion_tag('snippets/control.html')
def control(field, show_label='True', extra_classes='', use_placeholder=False):

    """ TODO: make render template depend on type of control """
    
    fieldtype = field.field.widget.__class__.__name__.lower()

    if fieldtype == "checkboxinput" or fieldtype == "integercheckboxwidget":
        show_label = False

    if use_placeholder:
        field.field.widget.attrs.update({"placeholder": field.label})
    
    return {'field': field,
            "show_label": show_label == 'True',
            'extra_classes': extra_classes,
            "use_placeholder": use_placeholder,
            'fieldtype': fieldtype}
