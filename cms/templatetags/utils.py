import django
from widget_tweaks.templatetags.widget_tweaks import add_class


register = django.template.Library()


@register.filter(name='multiply')
def multiply(value: int, args: int):
    return value * args


@register.filter(name='divide')
def divide(value: int, args: int):
    return value / args


@register.filter(name='add_validated_result_class')
def add_validated_result_class(field: django.forms.boundfield.BoundField, _=None):
    if hasattr(field, "errors") and field.errors:
        adding_class: str = 'is-invalid'
    elif field.data is not None:
        adding_class: str = 'is-valid'
    else:
        return field
    return add_class(field, adding_class)
