# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from utils import clear_internal_url
from urlparse import parse_qs

class AbstractAttachedBlock(models.Model):
    class Meta:
        abstract = True

    def admin_change_url(self):
        url = reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.module_name),  args=[self.pk] )
        return url

    def __unicode__(self):
        return '%s - %s' % (self.name, self.content)

class AttachedSimpleText(AbstractAttachedBlock):
    name = models.CharField(u'название блока', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    text = models.TextField(u'текстовый блок', blank=True)

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='simple_texts', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленный текст'
        verbose_name_plural = u'Блоки обычного текста'


class AttachedRichText(AbstractAttachedBlock):
    name = models.CharField(u'название блока', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    text = models.TextField(u'текстовый блок')

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='rich_texts', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленный форматированный текст'
        verbose_name_plural = u'Блоки форматированного текста'

    def html_stripped(self):
        from django.utils.html import strip_tags
        return strip_tags(self.text)
    html_stripped.short_description = u'текстовый блок'


class AttachedLink(AbstractAttachedBlock):
    name = models.CharField(u'название блока', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    title = models.CharField(u'текст ссылки', max_length=300, blank=True)
    link = models.CharField(u'ссылка', max_length=300)

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='links', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленная ссылка'
        verbose_name_plural = u'Ссылки'

    def save(self, *args, **kwargs):
        self.link = clear_internal_url(self.link)
        super(AttachedLink, self).save(*args, **kwargs)

class AttachedYoutubeVideo(AbstractAttachedBlock):
    name = models.CharField(u'название блока', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    title = models.CharField(u'название видео', max_length=300, blank=True)
    description = models.TextField(u'описание видео', blank=True)
    link = models.URLField(u'ссылка', help_text=u'ссылка на видео с Youtube.com', blank=True)

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='videos', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    def __unicode__(self):
        return '%s - %s' % (self.name, self.content)

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленное видео'
        verbose_name_plural = u'Прикрепленные видео'

    def thumbnail(self):
        if self.link:
            qs = self.link.split('?')
            video_id = parse_qs(qs[1])['v'][0]
            return '<img src="http://img.youtube.com/vi/%s/0.jpg" >' % video_id
        else:
            return None
    thumbnail.short_description = u'скриншот видео'
    thumbnail.allow_tags = True


