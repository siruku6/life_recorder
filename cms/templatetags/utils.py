from django import template


register = template.Library()


@register.filter(name="multiply")
def multiply(value, args):
    return value * args


@register.filter(name="divide")
def divide(value, args):
    return value / args
