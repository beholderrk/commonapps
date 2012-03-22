# -*- coding: utf-8 -*-
from django import template
from gblocks.models import SocialLink
from django.contrib.contenttypes.models import ContentType
from django_generic_flatblocks.models import GenericFlatblock

register = template.Library()

@register.inclusion_tag('gblocks/sociallink/all_social_links.html', takes_context=True)
def all_social_links(context):
    sl_content_type = ContentType.objects.get_for_model(SocialLink)
    social_links = GenericFlatblock.objects.filter(content_type = sl_content_type)
#    return {'social_links': social_links}
    context.update({'social_links': social_links})
    return context
