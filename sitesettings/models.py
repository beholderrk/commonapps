# -*- coding: utf-8 -*-
from django.db import models

class SettingsGroup(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(u'группа', max_length=100)

    class Meta:
        verbose_name = u'группу'
        verbose_name_plural = u'настройки'

    def __unicode__(self):
        return self.name


class Settings(models.Model):
    group = models.ForeignKey(SettingsGroup, related_name='settings')
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(u'название настройки', max_length=100)
    value = models.CharField(u'значение', max_length=1024)

    def __unicode__(self):
        return self.name

    @classmethod
    def get_value(cls, setting):
        return cls.objects.get(code = setting['code']).value