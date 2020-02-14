from django import template
register=template.Library()
from registration.models import CleanerModel

@register.simple_tag
def count():
    return CleanerModel.objects.count()