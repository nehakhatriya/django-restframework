from django.db import models
from django.conf import settings
from django.db.models import Q

User=settings.AUTH_USER_MODEL
# Create your models here.

class ProductQuerySet(models.QuerySet):
        def is_public(self):
             return self.filter(public=True)
        def search(self,query,user=None):
            lookup=Q(title__icontains=query) | Q(content__icontains=query)
            qs=self.is_public().filter(lookup)
            if user is not None:
                 qs=qs.filter(user=user)
            return qs
        
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self.db)
    
    def search(self,query,user=None):
        return self.get_queryset().search(query=query,user=user)

class Product(models.Model):
    public=models.BooleanField(default=True)
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title= models.TextField()
    content=models.TextField(null=True , blank=True)
    price=models.DecimalField(default=0.0,max_digits=15,decimal_places=2)

    def is_public(self):
         return self.public
    objects=ProductManager()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 122