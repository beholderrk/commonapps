# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions, AlreadyRegistered
    from models import *

    class AttachedSimpleTextTranslationOptions(TranslationOptions):
        fields=('title', 'text',)
    try:
        translator.register(AttachedSimpleText, AttachedSimpleTextTranslationOptions)
    except AlreadyRegistered:
        pass

    class AttachedRichTextTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    try:
        translator.register(AttachedRichText, AttachedRichTextTranslationOptions)
    except AlreadyRegistered:
        pass

    class AttachedLinkTranslationOptions(TranslationOptions):
        fields=('title',)

    try:
        translator.register(AttachedLink, AttachedLinkTranslationOptions)
    except AlreadyRegistered:
        pass

    class AttachedYoutubeVideoTranslationOptions(TranslationOptions):
        fields=('title', 'description')

    try:
        translator.register(AttachedYoutubeVideo, AttachedYoutubeVideoTranslationOptions)
    except AlreadyRegistered:
        pass


