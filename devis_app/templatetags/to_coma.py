from django import template

register = template.Library()

@register.filter
def to_coma(value):
    return str(value).replace(".",",")