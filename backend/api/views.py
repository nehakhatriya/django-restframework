from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.

@api_view(['POST'])
def api_home(request,*args,**kwargs):
        
        data_req=request.data
        serializer=ProductSerializer(data=data_req)
        if serializer.is_valid(raise_exception=True):
                serializer.save()
                print(serializer.data)
                return Response(serializer.data)
        else :
                return Response({"message":"Not valid data"})
        
        
# @api_view(['GET'])
# def api_home(request,*args,**kwargs):
        
#         instance=Product.objects.all().order_by('?').first()
#         data={}
#         if instance:
#                 #data= model_to_dict(instance,fields=['id','title','price'])
#                 data=ProductSerializer(instance).data

#         # body= request.body #string of json data
#         # data={}
#         # try:
#         #     data=json.loads(body) #string of json data -> pyhton dict
#         # except:
#         #       pass
#         # data['params']=dict(request.GET)
#         # data['headers']=dict(request.headers)
#         return Response(data)
