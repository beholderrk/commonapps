# -*- coding: utf-8 -*-
from django import template
import os

register = template.Library()

@register.filter()
def filetype(value):
    extension = os.path.splitext(value.path)[1].upper()
    return extension.lstrip('.')

@register.filter()
def filetypeicon(value):
    """
    Возвращает имя иконки соответствующей типу файла
    """
    extentions_list = ('pdf', 'doc', 'xls', 'html', 'swf')
    image_extentions_list = ('jpg', 'jpeg', 'png', 'gif', 'bmp')
    video_extentions_list = ('avi', 'divx', 'xvid', 'flv', 'mpeg', 'mpg')
    audio_extentions_list = ('mp3', 'wav', 'flac', 'ogg', 'wma')
    archive_extentions_list = ('zip', 'rar', 'tar', '7z')

    extension = os.path.splitext(value.path)[1].lower().lstrip('.')
    icon = 'txt.png'
    if extension in extentions_list:
        icon = '%s.png' % extension
    if extension in image_extentions_list:
        icon = 'img.png'
    if extension in video_extentions_list:
        icon = 'video.png'
    if extension in audio_extentions_list:
        icon = 'audio.png'
    if extension in archive_extentions_list:
        icon = 'compress.png'
    return icon