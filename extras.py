from django import template
from django.http import QueryDict

register = template.Library()


@register.filter(name='inc')
def inc(value, args):
    value = int(value) + int(args)
    return value


@register.simple_tag()
def division(a, b, to_int=False):
    if bool(to_int):
        return int(int(a)/int(b))
    else:
        return int(a)/int(b)
