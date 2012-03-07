# -*- coding: utf-8 -*-
# django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from sorl.thumbnail.shortcuts import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin
from slider.models import Slide, Slider

MODELTRANSLATION = bool(getattr(settings, "MODELTRANSLATION_TRANSLATION_REGISTRY", False))

if MODELTRANSLATION:
    from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline, TranslationAdmin

    class AdminBaseInline(TranslationStackedInline):
        pass
    class AdminBase(TranslationAdmin):pass
else:
    class AdminBaseInline(admin.StackedInline):
        pass
    class AdminBase(admin.ModelAdmin):pass

class SlideAdmin(AdminImageMixin, AdminBase):
    list_display = ["__unicode__", 'admin_image_preview', "display", 'position', ]
    list_editable = ["display", 'position', ]

    def admin_image_preview(self, obj):
        if obj.image:
            thumbnail = get_thumbnail(obj.image, '70')
            return '<a href="%s" target="blank"><image style="max-height:70px;max-width:70px" src="%s"/></a>' % (thumbnail.url, thumbnail.url)
        return ''
    admin_image_preview.short_description = _(u'превью')
    admin_image_preview.allow_tags = True

    if MODELTRANSLATION:
        class Media:
            js = settings.JS_MULTILANG
            css = settings.CSS_MULTILANG

class SlideInline(AdminInlineImageMixin, AdminBaseInline):
    model = Slide

class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slides_count']
    readonly_fields = ['name',]
    inlines = [SlideInline,]
    save_on_top = True

    def slides_count(self, obj):
        return obj.slides.count()
    slides_count.short_description = u'количество слайдов'

    if MODELTRANSLATION:
        class Media:
            js = settings.JS_MULTILANG
            css = settings.CSS_MULTILANG


admin.site.register(Slide, SlideAdmin)
admin.site.register(Slider, SliderAdmin)
