from django import forms
from .models import Inventory, Employee, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Signup Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Inventory Form
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'category', 'supplier', 'quantity', 'threshold']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),  # Dropdown for categories
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'threshold': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'role', 'shift', 'clock_in_time', 'clock_out_time']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),  # Dropdown for roles
            'shift': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter shift'}),
            'clock_in_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'clock_out_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'inventory_item', 'status', 'priority', 'due_date']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'inventory_item': forms.Select(attrs={'class': 'form-select'}),  # Dropdown for inventory items
            'status': forms.Select(attrs={'class': 'form-select'}),  # Dropdown for order status
            'priority': forms.Select(attrs={'class': 'form-select'}),  # Dropdown for priority
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


# Search Forms with Better Input Styling
class InventorySearchForm(forms.Form):
    name = forms.CharField(
        required=False, 
        label='Search by Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Inventory'})
    )


class EmployeeSearchForm(forms.Form):
    name = forms.CharField(
        required=False, 
        label='Search by Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Employee'})
    )


class OrderSearchForm(forms.Form):
    customer_name = forms.CharField(
        required=False, 
        label='Search by Customer Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Order'})
    )
