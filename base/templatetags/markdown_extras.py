from django import template
from django.template.defaultfilters import stringfilter

from markdown import markdown


register = template.Library()

@register.filter
@stringfilter
def to_markdown(text):
    return markdown(text, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.smarty',
    ])