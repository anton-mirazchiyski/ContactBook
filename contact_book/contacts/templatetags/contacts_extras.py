from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True, need_autoescape=True)
@stringfilter
def number_spacing(value, arg):
    """
    Adds spaces between the digits of a phone number
    """
    new_value = ''

    for i in range(len(value)):
        if i == len(value) - 1:
            break
        digit = value[i]
        new_value += digit

        count = i + 1
        if count % arg == 0:
            new_value += ' '

    return new_value
