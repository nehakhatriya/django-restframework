from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet,ProductGenericViewSet

router = DefaultRouter()

router.register('product',ProductViewSet,basename='product')

urlpatterns=router.urls