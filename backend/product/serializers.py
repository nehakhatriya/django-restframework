from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title,uniqure_validator
class ProductSerializer(serializers.ModelSerializer):

    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url= serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[validate_title,uniqure_validator])
    class Meta:
        model=Product
        fields=[
            'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def validate_title(self,value):
    #     qs=Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} already exists')
    #     return value
    
    def create(self,validated_data):
        email=validated_data.pop("email")
        return super().create(validated_data)


    def get_edit_url(self,obj):
        request=self.context.get('request')
        if request is None:
            return ""
        return reverse('product-edit',kwargs={'pk':obj.pk},request=request)
    
    def get_my_discount(self,obj):
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()