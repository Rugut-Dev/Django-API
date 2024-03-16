from rest_framework import serializers
from .models import Product, Product_variant


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_variant
        fields = '__all__'

    
