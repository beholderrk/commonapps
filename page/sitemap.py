from django.contrib.sitemaps import Sitemap
from page.models import Page, Action
from page.templatetags.page_tags import get_action_link

class ActionSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Action.objects.filter(active=True)

    def location(self, obj):
        return get_action_link(obj)