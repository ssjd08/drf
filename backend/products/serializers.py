from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(view_name="product-detail",
                                                      lookup_field="pk")
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    class Meta:
        model = Product
        fields = [
            'detail_url',
            'update_url',
            # 'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
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
    
    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     return obj
    
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product title.")
        
    #     return value