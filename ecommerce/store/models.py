from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)  # Name of the customer
    email = models.EmailField(unique=True)  # Email address
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number

    def __str__(self):
        return self.name  # Display the customer's name in the admin interface

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  # Foreign key relationship to the Customer model (one-to-many relationship)
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically add the order creation date
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # The total amount for the order
    status = models.CharField(max_length=20, default='Pending')  # Order status (e.g., Pending, Shipped)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"  # Display the order ID and customer name
