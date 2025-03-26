from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),  # Dashboard (index page after login)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Log out
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
]
