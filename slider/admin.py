# -*- coding: utf-8 -*-
# django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail.shortcuts import get_thumbnail
from slider.models import *
class SliderAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", 'admin_image_preview', "display", 'position', ]
    list_editable = ["display", 'position', ]

    def admin_image_preview(self, obj):
        if obj.image:
            thumbnail = get_thumbnail(obj.image, '70')
            return '<a href="%s" target="blank"><image style="max-height:70px;max-width:70px" src="%s"/></a>' % (thumbnail.url, thumbnail.url)
        return ''
    admin_image_preview.short_description = _(u'превью')
    admin_image_preview.allow_tags = True
admin.site.register(Slider)
