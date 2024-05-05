from rest_framework import viewsets,mixins
from product.serializers import ProductSerializer
from product.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    get -> list
    get -> retrieve
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'