# django imports
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from annoying.decorators import render_to

from page.models import Page

@render_to()
def page_view(request, slug):
    """Displays page with passed slug
    """
    page = get_object_or_404(Page, slug=slug)
    parts = page.page_blocks.filter(active = True)
    if request.user.is_superuser or page.active:
        return { 'TEMPLATE': page.template_name, 'page': page, 'parts': parts }
    raise Http404('No %s matches the given query.' % page._meta.object_name)



