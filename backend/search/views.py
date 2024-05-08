from django.shortcuts import render
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.
from rest_framework.response import Response
from . import client
class SearchListView(generics.GenericAPIView):
        def get(self,request,*args,**kwargs):
             user=None
             if request.user.is_authenticated:
                  user=request.user.username
             query=request.GET.get('q')
             public=request.GET.get('public') or None
             if not query:
                  return Response("",status=400)
             results=client.perform_search(query,public=public)
             return Response(results)


class SearchOldListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get_queryset(self,*args,**kwargs):
        qs= super().get_queryset(*args,**kwargs)
        q=self.request.GET.get('q')
        results=Product.objects.none()
        if q is not None:
            user=None
            if self.request.user.is_authenticated:
                user=self.request.user
                results=qs.search(q,user=user)        
        return results
    
