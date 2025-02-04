from django.shortcuts import render, redirect
from .models import Inventory, Employee, Order
from .forms import InventoryForm,EmployeeForm,OrderForm
from .forms import InventorySearchForm, EmployeeSearchForm, OrderSearchForm     #solved name error (should be defined) 
from django.shortcuts import get_object_or_404, redirect   #delete views 

def inventory_list(request):
    inventory = Inventory.objects.all()
    search_form = InventorySearchForm(request.GET)
    if search_form.is_valid():
        name = search_form.cleaned_data.get('name')
        if name:
            inventory = inventory.filter(name__icontains=name)
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'factory/inventory_list.html', {'inventory': inventory, 'form': form, 'search_form': search_form})

def employee_list(request):
    employees = Employee.objects.all()
    search_form = EmployeeSearchForm(request.GET)
    if search_form.is_valid():
        name = search_form.cleaned_data.get('name')
        if name:
            employees = employees.filter(name__icontains=name)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'factory/employee_list.html', {'employees': employees, 'form': form, 'search_form': search_form})

def order_list(request):
    orders = Order.objects.all()
    search_form = OrderSearchForm(request.GET)
    if search_form.is_valid():
        customer_name = search_form.cleaned_data.get('customer_name')
        if customer_name:
            orders = orders.filter(customer_name__icontains=customer_name)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'factory/order_list.html', {'orders': orders, 'form': form, 'search_form': search_form})



def edit_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'factory/edit_inventory.html', {'form': form})

def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'factory/edit_employee.html', {'form': form})

def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'factory/edit_order.html', {'form': form})



def delete_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    item.delete()
    return redirect('inventory_list')


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('order_list')