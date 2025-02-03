from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('orders/', views.order_list, name='order_list'),
]