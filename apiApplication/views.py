from django.shortcuts import render
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Product_variant
from .serializers import ProductSerializer


# Create your views here.
@api_view(['POST'])
def create_products(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        # Access and create variants
        variants_data = request.data.get('variants')
        for variant_data in variants_data:
            Product_variant.objects.create(product=product, **variant_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# bulk_create for products and product_variants
@api_view(['POST'])
def create_products_bulk(request):
    products_data = request.data
    products_to_create = []
    variants_to_create = []

    for product_data in products_data:
        product = Product(name=product_data['name'], image=product_data.get('image', ''))
        products_to_create.append(product)

        variants_data = product_data.get('variants')
        if variants_data:
            for variant_data in variants_data:
                variant = Product_variant(product_id=product, **variant_data)
                variants_to_create.append(variant)

    with transaction.atomic():
        Product.objects.bulk_create(products_to_create)
        batch_size = max(len(variants_to_create) // 10, 1)
        for i in range(0, len(variants_to_create), batch_size):
            batch = variants_to_create[i:i+batch_size]
            Product_variant.objects.bulk_create(batch)

    return Response("Products and variants created successfully", status=status.HTTP_201_CREATED)

# listing products
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
