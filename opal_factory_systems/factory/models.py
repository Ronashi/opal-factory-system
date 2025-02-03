from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255 )
    quantity = models.IntegerField()
    threshold = models.IntegerField()
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
      
    
    
