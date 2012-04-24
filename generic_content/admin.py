# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.conf import settings
from django.db import models
from django import forms
from django.contrib import admin
from models import AttachedLink, AttachedRichText, AttachedSimpleText, AttachedYoutubeVideo
from improved_inline.widgets import  CKEditorInline, CKEditor

MODELTRANSLATION = 'modeltranslation' in settings.INSTALLED_APPS

if MODELTRANSLATION:
    from modeltranslation.admin import TranslationStackedInline, TranslationAdmin, TranslationGenericTabularInline, TranslationGenericStackedInline

    class AdminBaseInline(TranslationGenericStackedInline): pass
    class AdminBase(TranslationAdmin): pass
    js_base = settings.JS_MULTILANG
    css_base = settings.CSS_MULTILANG
else:
    class AdminBaseInline(generic.GenericStackedInline): pass
    class AdminBase(admin.ModelAdmin): pass
    js_base = ()
    css_base = {}

class AbstractAttachedBlockInline(AdminBaseInline):
    ct_field = 'content_type'
    ct_fk_field = 'content_id'
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields

class AttachedSimpleTextInline(AbstractAttachedBlockInline):
    model = AttachedSimpleText
    exclude = ('name',)

class AttachedRichTextInline(AbstractAttachedBlockInline):
    model = AttachedRichText
    exclude = ('name',)
    formfield_overrides = {models.TextField: {'widget':CKEditorInline}}

class AttachedLinkInline(AbstractAttachedBlockInline):
    model = AttachedLink
    exclude = ('name',)

class AttachedYoutubeVideoInline(AbstractAttachedBlockInline):
    model = AttachedYoutubeVideo
    fields = ('name', 'title', 'position',)
    readonly_fields = ('title',)

class AttachedSimpleTextAdmin(AdminBase):
    fields = ('name','title', 'text', 'position',)

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedSimpleText, AttachedSimpleTextAdmin)

class AttachedRichTextAdmin(AdminBase):
    fields = ('name','title', 'text', 'position',)
    formfield_overrides = {models.TextField: {'widget':CKEditor}}

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedRichText, AttachedRichTextAdmin)

class AttachedLinkAdmin(AdminBase):
    fields = ('name', 'title', 'link', 'css_class', 'position',)

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedLink, AttachedLinkAdmin)

class AttachedYoutubeVideoAdmin(AdminBase):
    fields = ('name', 'link', 'title', 'description', 'thumbnail', 'position',)
    readonly_fields = ('thumbnail',)

    class Media:
        js = js_base
        css = css_base

admin.site.register(AttachedYoutubeVideo, AttachedYoutubeVideoAdmin)

