#!/usr/bin/python3
import time
import random
import requests


API_URL = 'http://localhost:8000/products/bulk_create/'

# Generates random product variants for a product
def generate_product_variants(product_id):
    num_variants = random.randint(5, 10)
    variants = []
    for i in range(num_variants):
        variant = {
            'sku': f'variant_sku_{product_id}_{i+1}',
            'name': f'Variant {i+1} for Product {product_id}',
            'price': round(random.uniform(1.99, 9.99), 2),
            'details': f'Details for Variant {i+1}',
        }
        variants.append(variant)
    return variants

# Generates products with variants and post to API
def feed_api_with_products(num_products=1000):
    start_time = time.time()
    products = []
    for i in range(1, num_products+1):
        product = {
            'name': f'Product {i}',
            'image': f'https://example.com/product_{i}.jpg',
            'variants': generate_product_variants(i)
        }
        products.append(product)

    response = requests.post(API_URL, json=products)
    if response.status_code == 201:
        print("Products and variants created successfully!")
    else:
        print("Error creating products and variants:", response.text)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

feed_api_with_products()
