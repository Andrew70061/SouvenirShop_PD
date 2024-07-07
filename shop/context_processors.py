from .models import ProductCategory
from django import template

def categories(request):
    return {'categories': ProductCategory.objects.all()}

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)