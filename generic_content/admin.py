# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.conf import settings
from django.db import models
from django import forms
from django.contrib import admin
from models import AttachedLink, AttachedRichText, AttachedSimpleText

MODELTRANSLATION = 'modeltranslation' in settings.INSTALLED_APPS

if MODELTRANSLATION:
    from modeltranslation.admin import TranslationStackedInline, TranslationAdmin, TranslationGenericTabularInline

    class AdminBaseInline(generic.GenericTabularInline): pass
    class AdminBase(TranslationAdmin): pass
    js_base = settings.JS_MULTILANG
    css_base = settings.CSS_MULTILANG
else:
    class AdminBaseInline(generic.GenericTabularInline): pass
    class AdminBase(admin.ModelAdmin): pass
    js_base = ()
    css_base = {}

class AbstractAttachedBlockInline(AdminBaseInline):
    ct_field = 'content_type'
    ct_fk_field = 'content_id'
    extra = 0
    template = "admin/page/tabular_for_gc.html"

class AttachedSimpleTextInline(AbstractAttachedBlockInline):
    model = AttachedSimpleText
    fields = ('name', 'text', 'position',)
    readonly_fields = ('text',)

class AttachedRichTextInline(AbstractAttachedBlockInline):
    model = AttachedRichText
    fields = ('name', 'html_stripped', 'position',)
    readonly_fields = ('html_stripped',)

class AttachedLinkInline(AbstractAttachedBlockInline):
    model = AttachedLink
    fields = ('name', 'title', 'position',)
    readonly_fields = ('title',)

class AttachedSimpleTextAdmin(AdminBase):
    fields = ('text', 'position',)

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedSimpleText, AttachedSimpleTextAdmin)

class AttachedRichTextAdmin(AdminBase):
    fields = ('text', 'position',)
    formfield_overrides = {models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}}

    class Media:
        js = js_base + (settings.MEDIA_URL + 'ckeditor/ckeditor.js',)
        css = css_base

admin.site.register(AttachedRichText, AttachedRichTextAdmin)

class AttachedLinkAdmin(AdminBase):
    fields = ('name', 'title', 'link', 'position',)

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedLink, AttachedLinkAdmin)
