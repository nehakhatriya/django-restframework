from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.TextField()
    content=models.TextField(null=True , blank=True)
    price=models.DecimalField(default=0.0,max_digits=15,decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 122