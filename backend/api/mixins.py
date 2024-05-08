from rest_framework.permissions import IsAdminUser
from .permissions import ProductPermission

class ProductPermissionMixin(ProductPermission):
    permission_classes=[IsAdminUser,ProductPermission]

class UserMixin():
    user_field='user'
    allow_staff_view=False
    def get_queryset(self):
        lookup_data={}
        lookup_data[self.user_field]=self.request.user
        if self.allow_staff_view and self.request.user.is_staff:
            return super().get_queryset()
        qs=super().get_queryset()
        return qs.filter(**lookup_data)
