# -*- coding: utf-8 -*-
# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageField
from django.conf import settings

class Slider(models.Model):
    """ Слайдер
    """

    try:
        SHOW_ON_CHOICES = settings.SLIDER_SHOW_ON_CHOICES
    except Exception as e:
        SHOW_ON_CHOICES = (
            ("main", u"главная"),
        )

    title = models.CharField(_(u'заголовок'), blank=True, max_length=250, help_text=_(u'Рабочее название для админки.'))
    show_on = models.CharField(_(u'показывать на'), default=u'main', max_length=250,
                               help_text=_(u'принадлежность к странице, на которой будет находиться слайд'),
                               choices=SHOW_ON_CHOICES)
    image = ImageField(_(u'изображение'), upload_to='slider')
    name = models.CharField(_(u'название'), blank=True, max_length=250, help_text=_(u'будет показываться при наведении на слайд; максимум 250 символов.'))
    url = models.CharField(_(u'ссылка'), blank=True, max_length=10000)
    target = models.BooleanField(_(u"открывать ссылку в новом окне"), default=False)
    display = models.BooleanField(_(u'отображать'), default=True)
    position = models.IntegerField(_(u'позиция'), default=100, help_text=_(u'номер для сортировки слайдов'))

    class Meta:
        ordering = ("-position", "show_on", )
        verbose_name = u"слайд"
        verbose_name_plural = u'слайды'

    def __unicode__(self):
        return u'%s: %s' % ( self.show_on, self.title)