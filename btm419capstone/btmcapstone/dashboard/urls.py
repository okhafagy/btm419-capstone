from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import warranty_view
from django.contrib.auth.views import LogoutView

app_name = 'dashboard'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),  # Dashboard (index page after login)
    path('logout/', LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact'),  # Example contact page,
    path('sales/', views.sales, name='sales'),
    path('add_new_product/', views.add_new_product, name='add_new_product'),
    path('see_all_products/', views.see_all_products, name='see_all_products'),
    path('see_all_dealerships/', views.see_all_dealerships, name='see_all_dealerships'),
    path('see_all_sales/', views.see_all_sales, name='see_all_sales'),
    path('purchase_fulfillment_status/', views.purchase_fulfillment_status, name='purchase_fulfillment_status'),
    path('new-product/', views.new_product, name='newproduct'),
    path('products/', views.product_list_view, name='product'),
    path('login/', views.login_view, name='login'),
    path('warranty/', warranty_view, name='warranty'),
    path('inventory/', views.inventory, name='inventory'),
    path('claims/', views.claims, name='claims'),
]
