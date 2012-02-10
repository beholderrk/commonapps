from django import forms
from django.db import models
from django.conf import settings

class LocationPickerWidgetGoogle(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'css/location_picker.css',
            )
        }
        js = (
            'http://maps.google.com/maps/api/js?sensor=false&language=ru',
            settings.STATIC_URL + 'js/jquery.location_picker_google.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidgetGoogle, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidgetGoogle, self).render(name, value, attrs)

class LocationFieldGoogle(models.CharField):

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidgetGoogle
        return super(LocationFieldGoogle, self).formfield(**kwargs)


class LocationPickerWidgetYandex(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'css/location_picker.css',
            )
        }
        js = (
            'http://api-maps.yandex.ru/1.1/index.xml?key='+ getattr(settings, 'YANDEX_MAPS_API_KEY', ''),
            settings.STATIC_URL + 'js/jquery.location_picker_yandex.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidgetYandex, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidgetYandex, self).render(name, value, attrs)

class LocationFieldYandex(models.CharField):

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidgetYandex
        return super(LocationFieldYandex, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^locationpicker\.widgets\.LocationFieldYandex"])
    add_introspection_rules([], ["^locationpicker\.widgets\.LocationFieldGoogle"])
except ImportError:
    pass