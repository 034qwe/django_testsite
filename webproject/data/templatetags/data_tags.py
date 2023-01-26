from django import template
from data.models import *


register = template.Library()


@register.simple_tag()
def get_Articles():
    return Articles.objects.all()