from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, ProductForm
from django.contrib import messages
from .models import Product

# Login view
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard:index')  # Redirect to index (which has the dashboard)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard:index')  # Redirect to index (which has the dashboard)
            else:
                form.add_error(None, 'Invalid credentials')  # Show error if credentials are invalid
    else:
        form = LoginForm()

    return render(request, 'dashboard/login.html', {'form': form})

# Signup view
def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'dashboard/signup.html', {'form': form})

# Dashboard (Index) view - only accessible after logging in
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

# Contact view (example)
def contact(request):
    return render(request, 'dashboard/contact.html')

# Sales view - displays sales links
@login_required
def sales(request):
    return render(request, 'dashboard/sales.html')

# Add New Product view
@login_required
def add_new_product(request):
    return render(request, 'dashboard/add_new_product.html')  # Make sure this template exists

# See All Products view
@login_required
def see_all_products(request):
    return render(request, 'dashboard/see_all_products.html')  # Make sure this template exists

# See All Dealerships view
@login_required
def see_all_dealerships(request):
    return render(request, 'dashboard/see_all_dealerships.html')  # Make sure this template exists

# See All Sales view
@login_required
def see_all_sales(request):
    return render(request, 'dashboard/see_all_sales.html')  # Make sure this template exists

# Purchase Fulfillment Status view
@login_required
def purchase_fulfillment_status(request):
    return render(request, 'dashboard/purchase_fulfillment_status.html')  # Make sure this template exists

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES to handle the image upload
        if form.is_valid():
            # Handle the logic for saving the product (you can create a model to store products)
            product_name = form.cleaned_data['product_name']
            price = form.cleaned_data['price']
            product_image = form.cleaned_data['product_image']

            # You can save the product in a model here (assuming you have a model called Product)
            # Product.objects.create(name=product_name, price=price, image=product_image)

            messages.success(request, 'Product added successfully!')
            return redirect('dashboard:sales')  # Redirect to sales page after success
    else:
        form = ProductForm()

    return render(request, 'dashboard/newproduct.html', {'form': form})

# View to handle displaying and adding products
def new_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard:product')  # Redirect to the page that displays all products
    else:
        form = ProductForm()

    return render(request, 'dashboard/newproduct.html', {'form': form})

# View to display all products
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product.html', {'products': products})

@login_required
def warranty_view(request):
    warranty_options = {
        "Rust Protection": {"value": "Rust protection", "price": 199.99},
        "Fabric Protection": {"value": "Fabric protection", "price": 149.99},
        "Paint Protection": {"value": "Paint protection", "price": 179.99},
        "VIN Etching": {"value": "VIN etching", "price": 99.99},
        "Extended Warranties": {"value": "Extended warranties", "price": 299.99},
    }

    selected_warranties = []
    total_price = 0.0

    if request.method == 'POST':
        selected_warranties = request.POST.getlist('warranty_choices')
        for item in selected_warranties:
            if item in warranty_options:
                total_price += warranty_options[item]["price"]

    return render(request, 'dashboard/warranty.html', {
        'warranty_options': warranty_options,
        'selected_warranties': selected_warranties,
        'total_price': round(total_price, 2),
    })
