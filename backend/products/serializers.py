from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse



class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(view_name="product-detail",
                                                      lookup_field="pk")
    
    def get_update_url (self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        
        return reverse('product-update', kwargs={"pk":obj.pk}, request= request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
    class Meta:
        model = Product
        fields = [
            'detail_url',
            'update_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]