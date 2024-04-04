from django.urls import path

from .views import  product_detail_view,create_list_product_view,update_product_view,delete_product_view,product_mixin_api

urlpatterns=[
    path('',product_mixin_api),
    path('<int:pk>/',product_detail_view),
    path('<int:pk>/update',update_product_view),
    path('<int:pk>/delete',delete_product_view),
]