from django.urls import path
from . import views


urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/delete/<int:id>/', views.delete_inventory, name='delete_inventory'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),
]
