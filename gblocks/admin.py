from django.contrib import admin
from django.contrib.contenttypes import generic
from gblocks.models import *
from django_generic_flatblocks.models import GenericFlatblock
from sorl.thumbnail.admin import AdminImageMixin
from django.conf import settings
from django import forms
from gblocks import models as gblocks_models
from generic_content.admin import AttachedSimpleTextInline, AttachedRichTextInline, AttachedLinkInline
from filesandimages.admin import AttachedFileInline, AttachedImageInline

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


for gblocks_models_item in settings.GBLOCKS_MODELS:
    admin.site.register(getattr(gblocks_models, gblocks_models_item), AbstractAdmin)

class CustomBlockAdmin(AdminBase):
    inlines = [AttachedSimpleTextInline, AttachedRichTextInline, AttachedLinkInline,
               AttachedFileInline, AttachedImageInline]

    class Media:
        js = js_base +  (settings.MEDIA_URL + 'ckeditor/ckeditor.js',settings.MEDIA_URL + 'fancybox/jquery.fancybox.pack.js',)
        css = css_base

admin.site.register(CustomBlock, CustomBlockAdmin)
