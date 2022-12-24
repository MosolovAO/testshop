from django import template
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/tags/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'category_selected': category_selected}
