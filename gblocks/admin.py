# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from gblocks.models import *
from django_generic_flatblocks.models import GenericFlatblock
from sorl.thumbnail.admin import AdminImageMixin
from django.conf import settings
from django import forms
from gblocks import models as gblocks_models
from generic_content.admin import AttachedSimpleTextInline, AttachedRichTextInline, AttachedLinkInline, \
    AttachedYoutubeVideoInline
from filesandimages.admin import AttachedFileInline, AttachedImageInline
import generic_content.admin as generic_content_admin
import filesandimages.admin as filesandimages_admin

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

class DisableDeleteFormSet(generic.BaseGenericInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(DisableDeleteFormSet, self).__init__(*args, **kwargs)
        self.can_delete = False

class GenericFlatblockInline(generic.GenericTabularInline):
    model = GenericFlatblock
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1
    max_num = 1
    readonly_fields = ['slug']
    formset = DisableDeleteFormSet

class AbstractAdmin(AdminImageMixin, AdminBase):
    list_display = ['__unicode__', 'get_slug']
    inlines = [GenericFlatblockInline,]
#    formfield_overrides = {models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}}

    def get_slug(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        flatblock = GenericFlatblock.objects.get(object_id=obj.pk, content_type = content_type)
        return flatblock.slug
    get_slug.short_description = u'уникальный код'

    class Media:
        js = js_base + (settings.MEDIA_URL + 'ckeditor/ckeditor.js', settings.STATIC_URL + 'js/ckeditor_show.js')
        css = css_base


for gblocks_models_item in settings.GBLOCKS_MODELS:
    admin.site.register(getattr(gblocks_models, gblocks_models_item), AbstractAdmin)

class CustomBlockAdmin(AdminBase):
    inlines = [AttachedSimpleTextInline, AttachedRichTextInline, AttachedLinkInline,
        AttachedImageInline, AttachedFileInline, AttachedYoutubeVideoInline]
    exclude = ('visible_inlines',)

    def change_view(self, request, object_id, extra_context=None):
        current_object = self.get_object(request, object_id)

        if current_object.visible_inlines:
            self.inlines = []
            for visible_inline in current_object.visible_inlines.split(','):
                inline_class = getattr(generic_content_admin, visible_inline, None) or getattr(filesandimages_admin, visible_inline, None)
                if inline_class:
                    self.inlines.append(inline_class)

        return super(CustomBlockAdmin, self).change_view(request, object_id, extra_context=None)

    class Media:
        js = js_base + (settings.STATIC_URL + 'js/collapsed_inline.js',)
        css = css_base

admin.site.register(CustomBlock, CustomBlockAdmin)
