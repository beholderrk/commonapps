# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions, AlreadyRegistered
    from models import *

    class TitleTranslationOptions(TranslationOptions):
        fields=('title',)

    try:
        translator.register(Title, TitleTranslationOptions)
    except AlreadyRegistered:
        pass

    class TextTranslationOptions(TranslationOptions):
        fields=('text',)

    try:
        translator.register(Text, TextTranslationOptions)
    except AlreadyRegistered:
        pass

    class TitleTextAndImageTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    try:
        translator.register(TitleTextAndImage, TitleTextAndImageTranslationOptions)
    except AlreadyRegistered:
        pass

    class MapTranslationOptions(TranslationOptions):
        fields=('title','balloon_text',)

    try:
        translator.register(Map, MapTranslationOptions)
    except AlreadyRegistered:
        pass

    class ImageTranslationOptions(TranslationOptions):
        fields=()

    try:
        translator.register(Image, ImageTranslationOptions)
    except AlreadyRegistered:
        pass

    class BannerTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    try:
        translator.register(Banner, BannerTranslationOptions)
    except AlreadyRegistered:
        pass

    class TitleTextAndClassTranslationOptions(TranslationOptions):
        fields=('title', 'text',)

    try:
        translator.register(TitleTextAndClass, TitleTextAndClassTranslationOptions)
    except AlreadyRegistered:
        pass

    class SocialLinkTranslationOptions(TranslationOptions):
        fields=('title',)

    try:
        translator.register(SocialLink, SocialLinkTranslationOptions)
    except AlreadyRegistered:
        pass

    class CustomBlockTranslationOptions(TranslationOptions):
        fields=()

    try:
        translator.register(CustomBlock, CustomBlockTranslationOptions)
    except AlreadyRegistered:
        pass






