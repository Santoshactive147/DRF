# models.py
from django.db import models
import uuid

class Product(models.Model):
    # Define the fields for the Product model
 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='detail')
    warranty_period = models.PositiveIntegerField(help_text="Warranty period in months")
    specifications = models.TextField(help_text="Additional product specifications")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Product weight in kg")
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return f"Details for {self.product.name}"