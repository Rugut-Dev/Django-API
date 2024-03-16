# Django API Project README

This Django API project provides endpoints for managing products and their variants.

## Endpoints

1. **Create Product**: Allows the creation of a single product with its variants.
   - Method: POST
   - URL: `/products/create/`
   - Body: JSON data representing the product and its variants.

2. **Get Products**: Retrieves all products.
   - Method: GET
   - URL: `/products/`

3. **Bulk Create Products**: Allows the creation of multiple products.
   - Method: POST
   - URL: `/products/bulk_create/`
   - Body: JSON array containing data for multiple products.