# -*- coding: utf-8 -*-
# django imports
from django.contrib.sitemaps import Sitemap, ping_google
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, resolve, Resolver404
from django.conf import settings
from django.contrib.contenttypes import generic

from mptt.models import MPTTModel
from filesandimages.models import AttachedImage, AttachedFile
from utils import locale_strip_path, clear_internal_url

class ActionGroup(models.Model):
    """Actions of a action group can be displayed on several parts of the web
    page.

    **Attributes**:

    name
        The name of the group.
    """
    name = models.CharField(blank=True, max_length=100, unique=True)

    class Meta:
        ordering = ("name", )
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'

    def __unicode__(self):
        return self.name

    def get_actions(self):
        """Returns the actions of this group.
        """
        return self.actions.filter(active=True)

class Action(MPTTModel):
    """A action is a link which belongs to a action groups.

    **Attributes**:

    group
        The belonging group.
    title
        The title of the menu tab.
    link
        The link to the object.
    active
        If true the tab is displayed.
    position
        the position of the tab within the menu.
    parent
        Parent tab to create a tree.
    """
    group = models.ForeignKey(ActionGroup, verbose_name=_(u"Group"), related_name="actions")
    title = models.CharField(_(u"Title"), max_length=40, blank=True,)
    link = models.CharField(_(u"Link"), blank=True, max_length=100, help_text='можно использовать шаблон reverse__["url name", (arg1, arg2), {"kwarg1": kwarg1} ]')
    active = models.BooleanField(_(u"Active"), default=True)
    position = models.IntegerField(_(u"Position"), default=999)
    parent = models.ForeignKey("self", verbose_name=_(u"Parent"), blank=True, null=True)
    page = models.ForeignKey('Page', verbose_name=_(u'Page'), related_name='actions', blank=True, null=True)
    images = generic.GenericRelation(AttachedImage, verbose_name=_(u'action images'),
        object_id_field="content_id", content_type_field="content_type")

    def __unicode__(self):
        return '%s - %s' % (self.group.name, self.title)

    class Meta:
        ordering=("position", )
        verbose_name = u'Элемент меню'
        verbose_name_plural = u'Элементы меню'

    def save(self, *args, **kwargs):
        if self.page:
            self.link = locale_strip_path(reverse('page_view', None, (), {'slug': self.page.slug}))[1]
            self.title = self.page.title
        super(Action, self).save(*args, **kwargs)



class Page(models.Model):
    """An simple HTML page, which may have an optional file to download.
    """
    try:
        TEMPLATE_CHOISES = settings.PAGE_TEMPLATE_CHOISES
    except Exception as e:
        TEMPLATE_CHOISES = (
            ("page/page.html", u"Текстовая страница"),
        )

    title = models.CharField(_(u"заголовок"), max_length=100)
    slug = models.CharField(_(u"Slug"), max_length=100, unique=True)
    template_name = models.CharField(_(u"Шаблон"), choices=TEMPLATE_CHOISES, max_length=300, default=TEMPLATE_CHOISES[0])
    active = models.BooleanField(_(u"опубликовать"), default=True)
    exclude_from_navigation = models.BooleanField(_(u"исключить из навигации"), default=False)
    position = models.IntegerField(_(u"позиция"), default=999)
#    page_blocks = models.ManyToManyField('PageBlock', related_name='pages_containing')

    body = models.TextField(_(u"текст"), blank=True,)
    short_text = models.TextField(_(u"краткое содержание"), blank=True,)
#    file = models.FileField(_(u"File"), blank=True, upload_to="files")
    
    class Meta: 
        ordering = ("position", )
        verbose_name = u"текстовая страница"
        verbose_name_plural = u'текстовые страницы'
        
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return "page_view", (), {"slug" : self.slug}

    def save(self, force_insert=False, force_update=False, *args, **kw):
        super(Page, self).save(*args, **kw)
        try:
            ping_google()
        except Exception:
            pass

class PagesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Page.objects.filter(active=True)


class PageBlock(models.Model):
    """Block for text page may contain text fields, images or files"""
    name = models.CharField(_(u'block name'), max_length=250)
    title = models.CharField(_(u'block title'), blank=True, max_length=400)
    body = models.TextField(_(u'block body'), blank=True)
    link = models.CharField(_(u'block link'), blank=True, max_length=500)
    images = generic.GenericRelation(AttachedImage, verbose_name=_(u'block images'),
        object_id_field="content_id", content_type_field="content_type")
    files = generic.GenericRelation(AttachedFile, verbose_name=_(u'block files'),
        object_id_field="content_id", content_type_field="content_type")
    position = models.IntegerField(_(u'Position'), default=999)
    active = models.BooleanField(_(u'Active'), default=True)
    page = models.ForeignKey(Page, verbose_name=_(u'Page'), blank=True, null=True, related_name='page_blocks')

    class Meta:
        ordering = ("position", )
        verbose_name = u'блок для текстовых страниц'
        verbose_name_plural = u'блоки для текстовых страниц'

    def __unicode__(self):
        return '%s - %s' % (self.page.title, self.name)

    def save(self, force_insert=False, force_update=False, *args, **kw):
        if self.link:
            self.link = clear_internal_url(self.link)
        super(PageBlock, self).save(*args, **kw)





