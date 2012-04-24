# django imports
from django.contrib import admin
from django import forms
from django.db import models
from page.models import *
from mptt.admin import FeinCMSModelAdmin
from filesandimages.admin import AttachedImageInline, AttachedFileInline
from django.conf import settings

MODELTRANSLATION = 'modeltranslation' in settings.INSTALLED_APPS

if MODELTRANSLATION:

    js_multilang = (
        settings.STATIC_URL + 'modeltranslation/js/force_jquery.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
        settings.STATIC_URL + 'modeltranslation/js/tabbed_translation_fields.js',
        )
    css_multilang = {
        'screen': (settings.STATIC_URL + 'modeltranslation/css/tabbed_translation_fields.css',),
        }
else:
    js_multilang = ()
    css_multilang = {}

if MODELTRANSLATION:
    from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline

    class ActionAdminBase(FeinCMSModelAdmin, TranslationAdmin):
        pass

    class ActionInlineBase(TranslationStackedInline):
        pass

    class PageAdminBase(TranslationAdmin):
        pass

    class PageBlockAdminBase(TranslationAdmin):
        pass

    class PageBlockInlineBase(TranslationTabularInline):
        pass
else:
    class ActionAdminBase(FeinCMSModelAdmin):
        pass

    class ActionInlineBase(admin.TabularInline):
        pass

    class PageAdminBase(admin.ModelAdmin):
        pass

    class PageBlockAdminBase(admin.ModelAdmin):
        pass

    class PageBlockInlineBase(admin.StackedInline):
        pass


class PageBlockInline(PageBlockInlineBase):
    model = PageBlock
    extra = 0
    template = "admin/page/tabular.html"
    fields = ['name', 'title', 'active', 'position']
    readonly_fields = ['title',]

page_css = { 'screen': (css_multilang.get('screen') or ()) + (settings.STATIC_URL + 'fancybox/jquery.fancybox.css',)}

class PageAdmin(PageAdminBase):
    """
    """
    prepopulated_fields = prepopulated_fields = {"slug": ("title",)}
    inlines = [PageBlockInline]
#    exclude = ['page_blocks']
    formfield_overrides = {
        models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}
    }

    class Media:
        js = js_multilang  + (settings.MEDIA_URL + 'ckeditor/ckeditor.js',
                              settings.STATIC_URL + 'fancybox/jquery.fancybox.pack.js',
                              settings.STATIC_URL + 'js/page_edit_form.js',)
        css = page_css

if getattr(settings, 'PAGE_SEO_MODULE', False):
    from rollyourown.seo.admin import get_inline, MetadataFormset
    from django.utils.importlib import import_module
    seomodule = import_module(getattr(settings, 'PAGE_SEO_MODULE'))
    attrs = {
        'max_num': len(settings.LANGUAGES),
        'extra': 1,
        'model': seomodule.SEOMetadata._meta.get_model('modelinstance'),
        'ct_field': "_content_type",
        'ct_fk_field': "_object_id",
        'formset': MetadataFormset,
        }
    get_inline_inst = type('MetadataInline', (generic.GenericStackedInline,), attrs)
    PageAdmin.inlines += [get_inline_inst]
    
admin.site.register(Page, PageAdmin)

class PageBlockAdmin(PageBlockAdminBase):
    inlines = [AttachedImageInline, AttachedFileInline]
    formfield_overrides = {
        models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}
    }

    class Media:
        js = js_multilang + (settings.MEDIA_URL + 'ckeditor/ckeditor.js',)
        css = css_multilang

admin.site.register(PageBlock, PageBlockAdmin)

class ActionInline(ActionInlineBase):
    model = Action
    extra = 1

class ActionGroupAdmin(admin.ModelAdmin):
    inlines = [ActionInline,]

    class Media:
        js = js_multilang
        css = css_multilang

admin.site.register(ActionGroup, ActionGroupAdmin)

class ActionAdmin(ActionAdminBase):
    list_filter = ('group',)
    list_display = ('__unicode__', 'active', 'group',)
    list_editable = ('active', 'group',)
    inlines = (AttachedImageInline,)

    class Media:
        js = js_multilang
        css = css_multilang

admin.site.register(Action, ActionAdmin)

