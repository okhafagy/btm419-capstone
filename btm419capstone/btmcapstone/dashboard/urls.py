
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'dashboard'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),  # Dashboard (index page after login)
    path('logout/', LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact'), 
    path('login/', views.login_view, name='login'), 
    # Sale
    path('sales/', views.sales, name='sales'),
    path('sales/dealerships/', views.three_dealership_inventory, name='three_dealership_inventory'),
    path('sales/history/', views.order_history, name='order_history'),
    path('sales/add/', views.order_inv, name='order_inv'),

    # Inventory
    path('inventory/sum/', views.inventory_sum, name='inventory_sum'),
    path('inventory/add/', views.add_purchase, name='add_purchase'),
    path('inventory/remove/', views.remove_purchase, name='remove_purchase'),
    path('inventory/log/', views.inventory_log, name='inventory_log'),
    # Claims
    path('claims/', views.claims, name='claims'),
    path('claim/submit/', views.submit_complaint, name='submit_complaint'),
    path('claim/list/', views.complaint_list, name='list'),
    path('claim/view/<int:complaint_id>/', views.view_complaint, name='view'), 
    # Inspections
    path('inspection/submit/', views.submit_inspection, name='submit_inspection'),
    path('inspection/list/', views.inspection_list, name='list_inspection'),
    path('inspection/view/<int:inspection_id>/', views.view_inspection, name='view_inspection'),
]
