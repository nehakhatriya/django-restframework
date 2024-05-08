from rest_framework import serializers

class UserProductInLineSerializer(serializers.Serializer):
        url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
        title=serializers.CharField(read_only=True)

class UserInlineSerializer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    # related_products=serializers.SerializerMethodField(read_only=True)

    # def get_related_products(self,obj):
    #     user=obj
    #     qs=user.product_set.all()[:5]
    #     return UserProductInLineSerializer(qs,many=True,context=self.context).data