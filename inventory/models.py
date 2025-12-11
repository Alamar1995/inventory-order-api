
from django.db import models

class Product(models.Model):
    """
    Represents an item in the inventory.
    """
    # id (PK) is automatically created by Django

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text='Price must be greater than or equal to 0.'
    )
    stock_quantity = models.IntegerField(
        default=0, 
        help_text='Current quantity in stock.'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name