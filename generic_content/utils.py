# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, resolve, Resolver404
from urlparse import urlparse

try:
    from localeurl.utils import strip_path as locale_strip_path
except ImportError:
    def locale_strip_path(path):
        return '', path

def clear_internal_url(url, return_reverse=False):
    """Внутренняя ссылка возвращается без локали, как относительная, внешняя ссылка не изменяется"""
    link = urlparse(url)
    path = link.path + ('#' + link.fragment if link.fragment else '') + ('?' + link.query if link.query else '')
    try:
        path = locale_strip_path(path)[1] # удаление локали
        view, args, kwargs = resolve(path) # проверка является ли ссылка внутренней
        if return_reverse:
            return reverse(view, args=args, kwargs=kwargs)
        else:
            return path
    except Resolver404:
        return url
