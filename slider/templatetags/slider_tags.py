from django import template
from django.template.loader import get_template, render_to_string
from django.template.context import RequestContext
from slider.models import Slider

register = template.Library()

class SliderNode(template.Node):
    def __init__(self, slider_name, var_name, template_name):
        self.slider_name = slider_name
        self.var_name = var_name
        self.template_name = template_name or 'slider/slider.html'

    def render(self, context):
        self.slider_name = template.Variable(self.slider_name).resolve(context)

        slider, success = Slider.objects.get_or_create(name = self.slider_name)
        slides = slider.slides.filter(display=True)
        if self.var_name:
            context[self.var_name] = slides
            return ''

        request = context.get('request')
        return render_to_string(self.template_name, {'slides': slides, 'slider': slider}, context_instance=RequestContext(request))

@register.tag('slider')
def do_slider(parser, token):
    ''' syntax
    {% slider slider_name %}
    {% slider slider_name as variable %}
    {% slider slider_name to 'path/to/template.html' %}
    '''
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError(u'{% slider %} tag required more args')

    slider_name = bits[1]
    var_name = None
    if len(bits) == 4 and bits[2] == 'as':
        var_name = bits[3]

    template_name = None
    if len(bits) == 4 and bits[2] == 'to':
        template_name = bits[3][1:-1]

    return SliderNode(slider_name, var_name, template_name)