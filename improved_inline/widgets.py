# -*- coding: utf-8 -*-
from django.conf import settings
from django import forms


class CKEditor(forms.Textarea):
    def __init__(self, attrs=None):
        # The 'rows' and 'cols' attributes are required for HTML correctness.
        default_attrs = {'cols': '40', 'rows': '10', 'class': 'ckeditor'}
        if attrs:
            default_attrs.update(attrs)
        super(CKEditor, self).__init__(default_attrs)

#    class Media:
#        js = (settings.MEDIA_URL + 'ckeditor/ckeditor.js',
#              settings.STATIC_URL + 'js/collapsed_inline.js',
#              settings.STATIC_URL + 'js/inlines.min.js')

    def _media(self):
        return forms.Media(
            js = (settings.MEDIA_URL + 'ckeditor/ckeditor.js',))
#                  settings.STATIC_URL + 'js/collapsed_inline.js',
#                  settings.STATIC_URL + 'js/ckeditor_inline.js',
#                  settings.STATIC_URL + 'js/inlines_improved.js'))
    media = property(_media)


class CKEditorInline(CKEditor):
    def __init__(self, attrs=None):
        # The 'rows' and 'cols' attributes are required for HTML correctness.
        default_attrs = {'cols': '40', 'rows': '10', 'class': 'ckeditor_inline'}
        if attrs:
            default_attrs.update(attrs)
        super(CKEditorInline, self).__init__(default_attrs)

    def _media(self):
        return forms.Media(
            js = (settings.MEDIA_URL + 'ckeditor/ckeditor.js',
                  settings.STATIC_URL + 'js/collapsed_inline.js',
                  settings.STATIC_URL + 'js/ckeditor_inline.js',
                  settings.STATIC_URL + 'js/inlines_improved.js'))
    media = property(_media)



