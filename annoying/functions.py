from django.shortcuts import _get_queryset
from django.conf import settings
from django.db.models.query import QuerySet

def get_object_or_None(klass, *args, **kwargs):
    """
    Uses get() to return an object or None if the object does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), a MultipleObjectsReturned will be raised if more than one
    object is found.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None

def get_first_or_None(qsinit, *args, **kwargs):
    if not qsinit:
        return None

    if isinstance(qsinit, list):
        try:
            return qsinit[0]
        except IndexError:
            return None

    if isinstance(qsinit, QuerySet):
        queryset = qsinit
    elif isinstance(qsinit, type):
        queryset = _get_queryset(qsinit)
    try:
        return queryset.filter(*args, **kwargs)[0]
    except IndexError:
        return None

def get_config(key, default):
    """
    Get settings from django.conf if exists,
    return default value otherwise

    example:

    ADMIN_EMAIL = get_config('ADMIN_EMAIL', 'default@email.com')
    """
    return getattr(settings, key, default)
