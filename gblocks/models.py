# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageField
from locationpicker.widgets import LocationFieldYandex, LocationFieldGoogle
from django.conf import settings
from django_generic_flatblocks.models import GenericFlatblock
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from filesandimages.models import AttachedFile, AttachedImage
from generic_content.models import AttachedSimpleText, AttachedRichText, AttachedLink


class Title(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TitleBlock) %s" % self.title

class Text(models.Model):
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        content_type = ContentType.objects.get_for_model(self)
        flatblock = GenericFlatblock.objects.get(object_id=self.pk, content_type = content_type)
        return "(TextBlock - %s) %s..." % (flatblock.slug ,self.text[:30])

class Image(models.Model):
    image = ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(ImageBlock) %s" % self.image

class TitleAndText(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(TitleAndTextBlock) %s" % self.title

class TitleTextAndImage(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image = ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(TitleTextAndImageBlock) %s" % self.title

class Map(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    balloon_text = models.TextField(_('balloon text'))
    location = LocationFieldGoogle(blank=True, max_length=255)

    def __unicode__(self):
        return "(MapBlock) %s " % self.title

    def get_coord_str(self):
        coord = self.location.split(',')
        if len(coord) > 1:
            return '%s,%s' % (coord[1], coord[0])

    def get_yandex_api_key(self):
        return settings.YANDEX_MAPS_API_KEY

class Banner(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    image = ImageField(_('image'), upload_to='gblocks/', blank=True, help_text='ширина изображения 320 пикселей')
    link = models.CharField(_('link'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)

    def __unicode__(self):
        return "(BannerBlock) %s" % self.title

class TitleTextAndClass(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True, help_text=_(u'Тут должен быть html-список.'))
    class_name = models.CharField(_('class'), max_length=255, blank=True)

    def __unicode__(self):
        return "(TitleTextAndClassBlock) %s" % self.title


class SocialLink(models.Model):
    SOCIAL_CHOICES = getattr(settings, 'SOCIAL_CHOICES', ())

    title = models.CharField(_('title'), max_length=255, blank=True)
    class_name = models.CharField(_('class'), max_length=255, blank=True, choices=SOCIAL_CHOICES)
    link = models.CharField(_('link'), max_length=255, blank=True)

    def __unicode__(self):
        return '(SocialLink) %s' % self.class_name


class CustomBlock(models.Model):
    images = generic.GenericRelation(AttachedImage, verbose_name=_(u'изображения'),
        object_id_field="content_id", content_type_field="content_type")
    files = generic.GenericRelation(AttachedFile, verbose_name=_(u'файлы'), object_id_field="content_id",
        content_type_field="content_type")
    simple_texts = generic.GenericRelation(AttachedSimpleText, object_id_field="content_id",
        content_type_field="content_type")
    rich_texts = generic.GenericRelation(AttachedRichText, object_id_field="content_id",
        content_type_field="content_type")
    links = generic.GenericRelation(AttachedLink, object_id_field="content_id",
        content_type_field="content_type")

    def __unicode__(self):
        content_type = ContentType.objects.get_for_model(self)
        flatblock = GenericFlatblock.objects.get(object_id=self.pk, content_type = content_type)
        return '(CustomBlock - %s)' % flatblock.slug