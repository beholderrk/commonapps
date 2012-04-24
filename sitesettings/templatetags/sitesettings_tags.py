from django import template
from sitesettings.models import Settings

register = template.Library()

@register.filter
def sitesettings(format, arg):
    return format % Settings.objects.get(code = arg).value