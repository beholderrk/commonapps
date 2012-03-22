# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions
    from models import *

    class TitleTranslationOptions(TranslationOptions):
        fields=('title',)

    translator.register(Title, TitleTranslationOptions)

    class TextTranslationOptions(TranslationOptions):
        fields=('text',)

    translator.register(Text, TextTranslationOptions)

    class TitleTextAndImageTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    translator.register(TitleTextAndImage, TitleTextAndImageTranslationOptions)

    class MapTranslationOptions(TranslationOptions):
        fields=('title','balloon_text',)

    translator.register(Map, MapTranslationOptions)

    class ImageTranslationOptions(TranslationOptions):
        fields=()

    translator.register(Image, ImageTranslationOptions)

    class BannerTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    translator.register(Banner, BannerTranslationOptions)

    class TitleTextAndClassTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    translator.register(TitleTextAndClass, TitleTextAndClassTranslationOptions)

    class SocialLinkTranslationOptions(TranslationOptions):
        fields=('title',)

    translator.register(SocialLink, SocialLinkTranslationOptions)






