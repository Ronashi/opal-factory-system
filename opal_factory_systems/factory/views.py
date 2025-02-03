from django.shortcuts import render
from .models import Inventory, Employee, Order

def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'factory/inventory_list.html', {'inventory': inventory})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'factory/employee_list.html', {'employees': employees})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'factory/order_list.html', {'orders': orders})
