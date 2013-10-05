from django import template
from django.utils import simplejson
from core.models import Tag

register = template.Library()


@register.inclusion_tag("core/tags.html")
def render_tags(**kwargs):
    tags = []
    for t in Tag.objects.filter(parent=None):
        tags.append(t.serializable_object())
    tags = simplejson.dumps(tags)
    return {"tags":tags}
