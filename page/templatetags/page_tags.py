# -*- coding: utf-8 -*-
from django.template import Node, TemplateSyntaxError
from django import template
from django.template.loader import render_to_string

from django.core.urlresolvers import reverse, resolve
from page.models import *
import json
from django.utils.html import strip_tags
from django.utils.translation import ugettext as _

register = template.Library()

def get_action_link(action):
    bits = action.link.split('__')
    if len(bits) > 1:
        reverse_data = bits[1]
        try:
            reverse_data = json.loads(reverse_data)
            action.link = reverse(reverse_data[0], args=reverse_data[1], kwargs=reverse_data[2])
        except Exception:
            action.link = '#'
    return action

def is_selected(action, request):
    for child in action.childs:
        if is_selected(child, request):
            return True
    if request.path.find(action.link) != -1:
        return True
    return False

def get_action_childs(action, request):
    childs = action.get_children().filter(active=True)
    for child in childs:
        child = get_action_link(child)
        child.childs = get_action_childs(child, request)
        child.selected = is_selected(child, request)
    return childs

class ActionsNode(Node):
    def __init__(self, group_name):
        self.group_name = group_name

    def render(self, context):
        request = context.get("request")
        context["actions"] = list(Action.tree.filter(active=True, group__name=self.group_name, parent=None))
        for action in context["actions"]:
            action = get_action_link(action)
            action.childs = get_action_childs(action, request)
            action.selected = is_selected(action, request)
        return ''


def do_actions(parser, token):
    """Returns the actions for the group with the given id.
    """
    bits = token.contents.split()
    len_bits = len(bits)
    if len_bits != 2:
        raise TemplateSyntaxError(_('%s tag needs group id as argument') % bits[0])

    return ActionsNode(bits[1])

register.tag('actions', do_actions)

@register.inclusion_tag('dummy.html', takes_context=True)
def current_action(context):
    request = context.get("request")
    actions = Action.objects.filter(active=True)
    for action in actions:
        action = get_action_link(action)
        if request.path.find(action.link) != -1:
            context['current_action'] = action
    return {}

@register.filter
def menu_has_selected(value):
    for item in value:
        if getattr(item, 'selected'):
            return True
    return False

