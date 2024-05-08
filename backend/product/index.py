from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index='is_public'
    field=[
        'title',
        'content',
        'price',
        'public',
        'user',
    ]
    settings={
        'searchableAttributes':['title','content'],
        'attributesForFaceting':['user','public']
    }