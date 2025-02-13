from django.db import models

# Inventory Model
class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('Resistor', 'Resistor'),
        ('Capacitor', 'Capacitor'),
        ('IC', 'Integrated Circuit'),
        ('PCB', 'Printed Circuit Board'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=255, db_index=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    quantity = models.IntegerField()
    threshold = models.IntegerField()
    supplier = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


# Employee Model
class Employee(models.Model):
    ROLE_CHOICES = [
        ('Engineer', 'Engineer'),
        ('Operator', 'Operator'),
        ('Technician', 'Technician'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Operator')
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    shift = models.CharField(max_length=50, blank=True, null=True)  # Example: "Morning", "Night"

    def __str__(self):
        return f"{self.name} ({self.role})"


# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
    ]

    customer_name = models.CharField(max_length=255)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)  # Track materials used
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Normal')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.status})"
