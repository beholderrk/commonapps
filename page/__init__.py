# -*- coding: utf-8 -*-
from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.translator import translator, TranslationOptions
    from models import Action, Page, PageBlock

    class ActionTranslationOptions(TranslationOptions):
        fields=('title',)

    if Action not in translator._registry:
        translator.register(Action, ActionTranslationOptions)

    class PageAdminTranslationOptions(TranslationOptions):
        fields=('title', 'body', 'short_text')

    if Page not in translator._registry:
        translator.register(Page, PageAdminTranslationOptions)

    class PageBLockTranslationOptions(TranslationOptions):
        fields=('title', 'body',)

    if PageBlock not in translator._registry:
        translator.register(PageBlock, PageBLockTranslationOptions)