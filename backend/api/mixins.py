from rest_framework.permissions import IsAdminUser
from .permissions import ProductPermission

class ProductPermissionMixin(ProductPermission):
    permission_classes=[IsAdminUser,ProductPermission]