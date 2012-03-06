# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions
    from models import Slide

    class SlideTranslationOptions(TranslationOptions):
        fields=('caption',)

    translator.register(Slide, SlideTranslationOptions)

