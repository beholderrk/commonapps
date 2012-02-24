# django imports
from django.contrib import admin
from django import forms
from django.db import models
from rollyourown.seo.admin import register_seo_admin, get_inline
from page.models import *
#from page.seo import SEOMetadata
from mptt.admin import FeinCMSModelAdmin
from filesandimages.admin import AttachedImageInline, AttachedFileInline
from django.conf import settings

#register_seo_admin(admin.site, SEOMetadata)

try:
    MULTILANGUAGE =  settings.PAGE_MULTILANGUAGE
except Exception as e:
    MULTILANGUAGE = False

if MULTILANGUAGE:

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

if MULTILANGUAGE:
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

    class ActionInlineBase(admin.StackedInline):
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
    fields = ['name', 'title']
    readonly_fields = ['title',]

page_css = { 'screen': css_multilang.get('screen') + (settings.STATIC_URL + 'fancybox/jquery.fancybox.css',)}

class PageAdmin(PageAdminBase):
    """
    """
    prepopulated_fields = prepopulated_fields = {"slug": ("title",)}
    inlines = [PageBlockInline]
#    exclude = ['page_blocks']

    class Media:
        js = js_multilang  + (settings.MEDIA_URL + 'ckeditor/ckeditor.js',
                              settings.STATIC_URL + 'fancybox/jquery.fancybox.pack.js',
                              settings.STATIC_URL + 'js/page_edit_form.js',)
        css = page_css
    
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

    class Media:
        js = js_multilang
        css = css_multilang

admin.site.register(Action, ActionAdmin)