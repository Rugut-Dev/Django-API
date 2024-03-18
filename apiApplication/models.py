from django.db import models

# Create your models here.
class Product(models.Model):
    # pass
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    
class Product_variant(models.Model):
    # pass
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True)
    # rltp
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        indexes = [
            models.Index(fields=['sku']),
        ]
