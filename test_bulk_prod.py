#!/usr/bin/python3
import time
import requests


base_url = 'http://127.0.0.1:8000/products/bulk_create/'

# input
single_product_data = {
    "name": "Product Name",
    "image": "https://example.com/product.jpg"
}

bulk_insert_data = [single_product_data] * 1000

start_time = time.time()

response = requests.post(base_url, json=bulk_insert_data)

end_time = time.time()

time_taken = end_time - start_time

if response.ok:
    print("Bulk insertion successful.")
    print("Time taken to insert 1000 products:", time_taken, "seconds")
else:
    print("Failed to insert products.")
    print("Status code:", response.status_code)
    print("Response text:", response.text)
