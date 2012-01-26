# -*- coding: utf-8 -*-
# django imports
from django.contrib.sitemaps import Sitemap, ping_google
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, resolve

from mptt.models import MPTTModel

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
    active = models.BooleanField(_(u"Active"), default=False)
    position = models.IntegerField(_(u"Position"), default=999)
    parent = models.ForeignKey("self", verbose_name=_(u"Parent"), blank=True, null=True)
    page = models.ForeignKey('Page', verbose_name=_(u'Page'), related_name='actions', blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.group.name, self.title)

    class Meta:
        ordering=("position", )
        verbose_name = u'Элемент меню'
        verbose_name_plural = u'Элементы меню'

    def save(self, *args, **kwargs):
        if self.page:
            self.link = reverse('page_view', None, (), {'slug': self.page.slug})
            self.title = self.page.title
        super(Action, self).save(*args, **kwargs)

class Page(models.Model):
    """An simple HTML page, which may have an optional file to download.
    """
    title = models.CharField(_(u"Title"), max_length=100)
    slug = models.CharField(_(u"Slug"), max_length=100)
    short_text = models.TextField(blank=True,)
    body = models.TextField(_(u"Text"), blank=True,)
    active = models.BooleanField(_(u"Active"), default=False)
    exclude_from_navigation = models.BooleanField(_(u"Exclude from navigation"), default=False)
    position = models.IntegerField(_(u"Position"), default=999)
    file = models.FileField(_(u"File"), blank=True, upload_to="files")
    
    class Meta: 
        ordering = ("position", )
        verbose_name = u"текстовая страница"
        verbose_name_plural = u'текстовые страницы'
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return ("page_view", (), {"slug" : self.slug})
    get_absolute_url = models.permalink(get_absolute_url)

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

