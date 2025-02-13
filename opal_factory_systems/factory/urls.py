from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/edit/<int:id>/', views.edit_inventory, name='edit_inventory'),
    path('inventory/delete/<int:id>/', views.delete_inventory, name='delete_inventory'),
    path('inventory/export/', views.export_inventory_csv, name='export_inventory_csv'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/edit/<int:id>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
