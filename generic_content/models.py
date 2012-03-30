# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

class AbstractAttachedBlock(models.Model):
    class Meta:
        abstract = True

    def admin_change_url(self):
        url = reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.module_name),  args=[self.pk] )
        return url

class AttachedSimpleText(AbstractAttachedBlock):
    name = models.CharField(u'название', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    text = models.TextField(u'текстовый блок', blank=True)

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='simple_texts', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленный текст'
        verbose_name_plural = u'Прикрепленные тексты'


class AttachedRichText(AbstractAttachedBlock):
    name = models.CharField(u'название', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    text = models.TextField(u'текстовый блок')

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='rich_texts', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленный форматированный текст'
        verbose_name_plural = u'Прикрепленные форматированные тексты'

    def html_stripped(self):
        from django.utils.html import strip_tags
        return strip_tags(self.text)
    html_stripped.short_description = u'текстовый блок'


class AttachedLink(AbstractAttachedBlock):
    name = models.CharField(u'название', max_length=100)
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    title = models.CharField(u'текст ссылки', max_length=300, blank=True)
    link = models.CharField(u'ссылка', max_length=300)

    content_type = models.ForeignKey(ContentType, verbose_name=u'тип контента', related_name='links', blank=True, null=True)
    content_id = models.PositiveIntegerField(u'id контента', blank=True, null=True)
    content = generic.GenericForeignKey(ct_field='content_type', fk_field='content_id')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленная ссылка'
        verbose_name_plural = u'Прикрепленные ссылки'

