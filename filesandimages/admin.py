from django.contrib.contenttypes import generic
from filesandimages.models import AttachedImage, AttachedFile
from sorl.thumbnail.admin import AdminImageMixin

class AttachedImageInline(AdminImageMixin, generic.GenericTabularInline):
    model = AttachedImage
    ct_field = 'content_type'
    ct_fk_field = 'content_id'
    extra = 1

class AttachedFileInline(generic.GenericTabularInline):
    model = AttachedFile
    ct_field = 'content_type'
    ct_fk_field = 'content_id'
    extra = 1
