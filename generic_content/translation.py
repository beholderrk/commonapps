# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions
    from models import *

    class AttachedSimpleTextTranslationOptions(TranslationOptions):
        fields=('text',)

    translator.register(AttachedSimpleText, AttachedSimpleTextTranslationOptions)

    class AttachedRichTextTranslationOptions(TranslationOptions):
        fields=('text',)

    translator.register(AttachedRichText, AttachedRichTextTranslationOptions)

    class AttachedLinkTranslationOptions(TranslationOptions):
        fields=('title',)

    translator.register(AttachedLink, AttachedLinkTranslationOptions)

