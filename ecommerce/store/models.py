from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField(unique=True)  # Customer's email
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number

    def __str__(self):
        return self.name  # This makes the admin display the name for this model

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically sets the date when the order is created
    status = models.CharField(max_length=20, default='Pending')  # Order status (e.g., Pending, Shipped)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
