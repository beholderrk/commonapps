# -*- coding: utf-8 -*-
# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageField

class Slider(models.Model):
    name = models.CharField(_(u'название'), max_length=250, help_text=_(u'название говорит о том где будет использован этот слайдер'))
    options = models.TextField(_(u'опции'), blank=True)

    class Meta:
        verbose_name = u"слайдер"
        verbose_name_plural = u'слайдеры'

    def __unicode__(self):
        return u'%s' % self.name

class Slide(models.Model):
    """ Слайдер
    """
    slider = models.ForeignKey(Slider, verbose_name=_(u'слайдер'),
                               help_text=_(u'выберите к какому сладеру будет относиться данных слайд'), blank=True, related_name='slides')
    image = ImageField(_(u'изображение'), upload_to='slider', blank=True)
    name = models.CharField(_(u'название'), blank=True, max_length=250, help_text=_(u'будет показываться при наведении на слайд; максимум 250 символов.'))
    caption = models.TextField(_(u'подпись'), blank=True)
    url = models.CharField(_(u'ссылка'), blank=True, max_length=1000)
    target = models.BooleanField(_(u"открывать ссылку в новом окне"), default=False)
    display = models.BooleanField(_(u'отображать'), default=True)
    position = models.IntegerField(_(u'позиция'), default=100, help_text=_(u'номер для сортировки слайдов'))

    class Meta:
        ordering = ("-position", )
        verbose_name = u"слайд"
        verbose_name_plural = u'слайды'

    def __unicode__(self):
        return u'%s' % self.name