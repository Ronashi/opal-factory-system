from django.contrib import admin
from .models import Inventory, Employee, Order


admin.site.register(Inventory)
admin.site.register(Employee)
admin.site.register(Order)
