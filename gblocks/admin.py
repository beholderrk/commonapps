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

class GenericFlatblockInline(generic.GenericTabularInline):
    model = GenericFlatblock
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1
    max_num = 1
    readonly_fields = ['slug']

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
        AttachedImageInline, AttachedFileInline, AttachedYoutubeVideoInline]
    exclude = ('visible_inlines',)

    def change_view(self, request, object_id, extra_context=None):
        current_object = self.get_object(request, object_id)

        if current_object.visible_inlines:
            self.inline_instances = []
            for visible_inline in current_object.visible_inlines.split(','):
                inline_class = getattr(generic_content_admin, visible_inline, None) or getattr(filesandimages_admin, visible_inline, None)
                if inline_class:
                    self.inline_instances.append(inline_class(self.model, self.admin_site))
        else:
            self.inline_instances = [AttachedSimpleTextInline(self.model, self.admin_site),
                                     AttachedRichTextInline(self.model, self.admin_site),
                                     AttachedLinkInline(self.model, self.admin_site),
                                     AttachedImageInline(self.model, self.admin_site),
                                     AttachedFileInline(self.model, self.admin_site),
                                     AttachedYoutubeVideoInline(self.model, self.admin_site)]

        return super(CustomBlockAdmin, self).change_view(request, object_id, extra_context=None)

    class Media:
        js = js_base + (settings.STATIC_URL + 'js/collapsed_inline.js',)
        css = css_base

admin.site.register(CustomBlock, CustomBlockAdmin)
