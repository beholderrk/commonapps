from django.contrib import admin
from django.contrib.contenttypes import generic
from gblocks.models import *
from django_generic_flatblocks.models import GenericFlatblock
from sorl.thumbnail.admin import AdminImageMixin
from django.conf import settings
from django import forms
from gblocks import models as gblocks_models

MODELTRANSLATION = 'modeltranslation' in settings.INSTALLED_APPS

if MODELTRANSLATION:
    from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline, TranslationAdmin

    class AdminBaseInline(TranslationStackedInline): pass
    class AdminBase(TranslationAdmin): pass
    js_base = settings.JS_MULTILANG
    css_base = settings.CSS_MULTILANG
else:
    class AdminBaseInline(admin.TabularInline): pass
    class AdminBase(admin.ModelAdmin): pass
    js_base = ()
    css_base = {}

class GenericFlatblockInline(generic.GenericTabularInline):
    model = GenericFlatblock
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1
    max_num = 1

class AbstractAdmin(AdminImageMixin, AdminBase):
    inlines = [GenericFlatblockInline,]

    formfield_overrides = {models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}}
    class Media:
        js = js_base +  (settings.MEDIA_URL + 'ckeditor/ckeditor.js',)
        css = css_base

#admin.site.register(Title, AbstractAdmin)
#admin.site.register(Text, AbstractAdmin)
##admin.site.register(Image, AbstractAdmin)
#admin.site.register(getattr(gblocks_models, 'Image'), AbstractAdmin)
##admin.site.register(TitleAndText, AbstractAdmin)
#admin.site.register(TitleTextAndImage, AbstractAdmin)
#admin.site.register(Map, AbstractAdmin)
##admin.site.register(Banner, AbstractAdmin)
##admin.site.register(TitleTextAndClass, AbstractAdmin)

for gblocks_models_item in settings.GBLOCKS_MODELS:
    admin.site.register(getattr(gblocks_models, gblocks_models_item), AbstractAdmin)