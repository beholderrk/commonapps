# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from sorl.thumbnail.fields import ImageField

# Create your models here.
class AttachedImage(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=u"тип контента", related_name="images", blank=True, null=True)
    content_id = models.PositiveIntegerField(u"id контента", blank=True, null=True)
    content = generic.GenericForeignKey(ct_field="content_type", fk_field="content_id")
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    image = ImageField(upload_to='generic/images', verbose_name=u'изображение')
    title = models.CharField(max_length=250, verbose_name=u'название', null=True, blank=True)

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленное изображение'
        verbose_name_plural = u'Прикрепленные изображения'

class AttachedFile(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=u"тип контента", related_name="files", blank=True, null=True)
    content_id = models.PositiveIntegerField(u"id контента", blank=True, null=True)
    content = generic.GenericForeignKey(ct_field="content_type", fk_field="content_id")
    position = models.PositiveSmallIntegerField(u'позиция', default=999)
    file = models.FileField(upload_to='generic/files', verbose_name=u'прикрепленный файл')
    title = models.CharField(max_length=250, verbose_name=u'название')

    class Meta:
        ordering = ('position',)
        verbose_name = u'объект - Прикрепленный файл'
        verbose_name_plural = u'Прикрепленные файлы'