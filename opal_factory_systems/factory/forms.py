from django import forms
from .models import Inventory, Employee, Order

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity', 'threshold']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'clock_in_time', 'clock_out_time']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'status']
        

class InventorySearchForm(forms.Form):
    name = forms.CharField(required=False, label='Search by Name')

class EmployeeSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Search by Name')

class OrderSearchForm(forms.Form):
    customer_name = forms.CharField(required=False, label='Search by Customer Name')       