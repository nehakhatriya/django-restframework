from rest_framework import generics,mixins

from .models import Product
from .serializers import ProductSerializer

class CreateListProductApiview(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        if content is None:
            content=title
        serializer.save(content=content)

create_list_product_view=CreateListProductApiview.as_view()

# class CreateProductApiview(generics.CreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

#     def perform_create(self, serializer):
#         title=serializer.validated_data.get('title')
#         content=serializer.validated_data.get('content')
#         if content is None:
#             content=title
#         serializer.save(content=content)

class UpdateProductApiview(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_update(self, serializer):
        instance=serializer.save()
        instance.content=instance.title
        ##

update_product_view=UpdateProductApiview.as_view()

class DeleteProductApiview(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
        ##

delete_product_view=DeleteProductApiview.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'

product_detail_view=ProductDetailApiView.as_view()

class ProductMixInView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self, serializer):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')
            if content is None:
                content=title
            serializer.save(content=content)
    
product_mixin_api=ProductMixInView.as_view()