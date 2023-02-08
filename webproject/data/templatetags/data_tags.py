from django import template
from data.models import *


register = template.Library()


@register.simple_tag()
def get_Articles():
    return Category_Articles.objects.all()