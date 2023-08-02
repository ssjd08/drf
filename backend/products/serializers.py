from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    def get_my_discount(self, obj):
        return obj.get_discount
    
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]