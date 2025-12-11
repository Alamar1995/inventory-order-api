from django.db import models
from django.conf import settings
from inventory.models import Product

# Define choices for the Order Status field
ORDER_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('SHIPPED', 'Shipped'),
    ('CANCELLED', 'Cancelled'),
]

class Order(models.Model):
    """
    Represents an Order placed by a User.
    (1-to-many relationship with Users)
    """
    # Foreign Key to the CustomUser model defined in settings.py
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text='The user who placed the order.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS_CHOICES,
        default='PENDING',
        help_text='Current fulfillment status of the order.'
    )
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0.00,
        help_text='The calculated total cost of the order.'
    )

    class Meta:
        
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    """
    Represents a line item within a specific Order.
    (1-to-many relationship with Order and Product)
    """
    # Foreign Key to the Order
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        help_text='The order this item belongs to.'
    )
    # Foreign Key to the Product
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT, # Prevents deleting a Product that is part of a historical Order
        related_name='order_lines',
        help_text='The product being ordered.'
    )
    quantity = models.IntegerField()
    # Storing unit_price at the time of order is crucial for historical accuracy
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # Ensures no duplicate products in the same order, although you might allow it 
        # and just sum the quantities in the application logic. For now, this is safer.
        unique_together = ('order', 'product') 

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
