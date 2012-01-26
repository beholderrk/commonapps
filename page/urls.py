from django.conf.urls.defaults import *

urlpatterns = patterns('page.views',
    url(r'^(?P<slug>[-\w]*)$', "page_view", name="page_view"),
)