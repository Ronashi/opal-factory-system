from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import csv
from .models import Inventory, Employee, Order
from .forms import (
    InventoryForm, EmployeeForm, OrderForm,
    InventorySearchForm, EmployeeSearchForm, OrderSearchForm,
    SignUpForm
)

# CSV Export
@login_required
@user_passes_test(lambda u: u.is_superuser)
def export_inventory_csv(request):
    inventory = Inventory.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Category', 'Quantity', 'Supplier', 'Last Updated'])

    for item in inventory:
        writer.writerow([item.id, item.name, item.category, item.quantity, item.supplier, item.last_updated])

    return response


# User Registration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'factory/signup.html', {'form': form})


# Inventory View
@login_required
def inventory_list(request):
    inventory = Inventory.objects.all()
    search_form = InventorySearchForm(request.GET)
    if search_form.is_valid() and search_form.cleaned_data.get('name'):
        inventory = inventory.filter(name__icontains=search_form.cleaned_data['name'])

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item added successfully.")
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    
    return render(request, 'factory/inventory_list.html', {'inventory': inventory, 'form': form, 'search_form': search_form})


# Employee View
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    search_form = EmployeeSearchForm(request.GET)
    if search_form.is_valid() and search_form.cleaned_data.get('name'):
        employees = employees.filter(name__icontains=search_form.cleaned_data['name'])

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'factory/employee_list.html', {'employees': employees, 'form': form, 'search_form': search_form})


# Order View
@login_required
def order_list(request):
    orders = Order.objects.all()
    search_form = OrderSearchForm(request.GET)
    if search_form.is_valid() and search_form.cleaned_data.get('customer_name'):
        orders = orders.filter(customer_name__icontains=search_form.cleaned_data['customer_name'])

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order placed successfully.")
            return redirect('order_list')
    else:
        form = OrderForm()
    
    return render(request, 'factory/order_list.html', {'orders': orders, 'form': form, 'search_form': search_form})


# Dashboard View
@login_required
def dashboard(request):
    context = {
        'total_inventory': Inventory.objects.count(),
        'total_employees': Employee.objects.count(),
        'total_orders': Order.objects.count(),
        'completed_orders': Order.objects.filter(status='Completed').count(),
        'pending_orders': Order.objects.filter(status='Pending').count(),
        'recent_orders': Order.objects.order_by('-created_at')[:5],
    }
    return render(request, 'factory/dashboard.html', context)


# Edit Inventory
@login_required
def edit_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item updated successfully.")
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'factory/edit_inventory.html', {'form': form})


# Edit Employee
@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee details updated successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'factory/edit_employee.html', {'form': form})


# Edit Order
@login_required
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully.")
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'factory/edit_order.html', {'form': form})


# Delete Inventory (Only Admins)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    item.delete()
    messages.success(request, "Inventory item deleted successfully.")
    return redirect('inventory_list')


# Delete Employee (Only Admins)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('employee_list')


# Delete Order (Only Admins)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, "Order deleted successfully.")
    return redirect('order_list')
