# django imports
from django.contrib import admin
from django import forms
from django.db import models
from django.conf import settings
from rollyourown.seo.admin import register_seo_admin, get_inline
from page.models import *
#from page.seo import SEOMetadata
from mptt.admin import FeinCMSModelAdmin

#register_seo_admin(admin.site, SEOMetadata)

class PageAdmin(admin.ModelAdmin):
    """
    """
    prepopulated_fields = prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}
    }

    class Media:
        js = (settings.MEDIA_URL + 'ckeditor/ckeditor.js',)
    
admin.site.register(Page, PageAdmin)

class ActionInline(admin.TabularInline):
    model = Action
    extra = 1

class ActionGroupAdmin(admin.ModelAdmin):
    inlines = [ActionInline,]

admin.site.register(ActionGroup, ActionGroupAdmin)

class ActionAdmin(FeinCMSModelAdmin):
    list_filter = ('group',)
    list_display = ('__unicode__', 'active', 'group',)
    list_editable = ('active', 'group',)

admin.site.register(Action, ActionAdmin)