from django.shortcuts import render
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

# bulk_create for products only
# @api_view(['POST'])
# def create_products_bulk(request):
#     products_data = request.data
#     # Create a list of Product objects from the JSON data
#     products = [Product(name=item['name'], image=item.get('image', '')) for item in products_data]
#     Product.objects.bulk_create(products)
#     return Response("Products created successfully", status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_products_bulk(request):
    products_data = request.data
    products = [Product(name=item['name'], image=item.get('image', '')) for item in products_data]
    # Bulk create products
    Product.objects.bulk_create(products)
    
    # Create variants if provided
    for product, product_data in zip(products, products_data):
        variants_data = product_data.get('variants')
        if variants_data:
            product_variants = [Product_variant(product_id=product, **variant) for variant in variants_data]
            Product_variant.objects.bulk_create(product_variants)
    return Response("Products and variants created successfully", status=status.HTTP_201_CREATED)

# listing products
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
