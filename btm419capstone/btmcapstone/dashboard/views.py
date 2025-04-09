from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import InventoryLog
from .models import Inventory
from .purchaseform import PurchaseForm
from django.db.models import Sum
from .models import Complaint
from .complaintform import ComplaintForm
from .models import Inspection
from .inspectionform import InspectionForm
from .models import Sale
from .forms import SaleForm


#Inventory
def inventory_sum(request):
    inventory_logs = InventoryLog.objects.all()
    inventory_sums = InventoryLog.objects.values('inventory_id').annotate(total_count=Sum('quantity'))

    return render(request, 'dashboard/inventory_sum.html', {'inventory_sums': inventory_sums})


def inventory_log(request):
    inventory_logs = InventoryLog.objects.all()
    for log in inventory_logs:
        log.total_value = log.quantity * log.per_unit_value    
    return render(request, 'dashboard/inventory_log.html', {'inventory_logs': inventory_logs})


def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/log/')
    else:
        form = PurchaseForm()
    return render(request, 'dashboard/add_purchase.html', {'form': form})


def remove_purchase(request):
    if request.method == 'POST':
        purchase_id = request.POST.get('purchase_id')
        InventoryLog.objects.filter(purchase_id=purchase_id).delete()
        return redirect('/inventory/log/')
    else:
        purchase_ids = InventoryLog.objects.values_list('purchase_id', flat=True).distinct()
        return render(request, 'dashboard/remove_purchase.html', {'purchase_ids': purchase_ids})
    


# Login view
def login_view(request):
    
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

# Home Page
def index(request):
    return render(request, 'dashboard/index.html')

# Contact view
def contact(request):
    return render(request, 'dashboard/contact.html')

# Sales view - displays sales links
def sales(request):
    orders = Sale.objects.all().order_by('-actual_delivery_date')  # get all orders
    return render(request, 'dashboard/sales.html', {'orders': orders})

def order_history(request):
    sales = Sale.objects.all()
    return render(request, 'dashboard/order_history.html', {'sales': sales})

def order_inv(request):
    if request.method == 'POST':
        Sale.objects.create(
            sale_number=request.POST.get('sale_number'),
            dealership=request.POST.get('dealership'),
            product=request.POST.get('product'),
            quantity=request.POST.get('quantity'),
            expected_delivery_date=request.POST.get('expected_delivery_date'),
            actual_delivery_date=request.POST.get('actual_delivery_date')
        )
        return redirect('dashboard:sales')

    return render(request, 'dashboard/order_inv.html')

def three_dealership_inventory(request):
    # Get inventories per dealership
    quebec_inventory = (
        Sale.objects.filter(dealership__iexact='Quebec')
        .values('product')
        .annotate(stock=Sum('quantity'))
        .order_by('product')
    )
    mckernan_inventory = (
        Sale.objects.filter(dealership__iexact='McKernan')
        .values('product')
        .annotate(stock=Sum('quantity'))
        .order_by('product')
    )
    lachute_inventory = (
        Sale.objects.filter(dealership__iexact='Lachute')
        .values('product')
        .annotate(stock=Sum('quantity'))
        .order_by('product')
    )

    return render(request, 'dashboard/three_dealership_inventory.html', {
        'quebec_inventory': quebec_inventory,
        'mckernan_inventory': mckernan_inventory,
        'lachute_inventory': lachute_inventory
    })


#Claims

def claims(request):
    complaints = Complaint.objects.order_by('-date_added')
    inspections = Inspection.objects.order_by('-date_added')
    return render(request, 'dashboard/claims.html', {
        'complaints': complaints,
        'inspections': inspections
    })

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            claim = form.save()  
            return redirect('dashboard:view', complaint_id=claim.id)  
    else:
        form = ComplaintForm()
    return render(request, 'dashboard/submit_complaint.html', {'form': form})

def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-date_added')
    return render(request, 'dashboard/complaint_list.html', {'complaints': complaints})


def view_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    return render(request, 'dashboard/view_complaint.html', {'complaint': complaint})

#Inspections

def submit_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save()  
            return redirect('dashboard:view_inspection', inspection_id=inspection.id)  
    else:
        form = InspectionForm()
    return render(request, 'dashboard/submit_inspection.html', {'form': form})


def inspection_list(request):
    if request.method == 'POST':
        inspection_id = request.POST.get('update_id')
        if inspection_id:
            try:
                inspection = Inspection.objects.get(id=inspection_id)
                date_str = request.POST.get(f'estimated_date_{inspection_id}')
                if date_str:
                    inspection.estimated_date = date_str
                    inspection.save()
            except Inspection.DoesNotExist:
                pass
        return redirect('dashboard:list_inspection')

    inspections = Inspection.objects.all().order_by('-date_added')
    return render(request, 'dashboard/inspection_list.html', {'inspections': inspections})


def view_inspection(request, inspection_id):
    inspection = Inspection.objects.get(id=inspection_id)
    return render(request, 'dashboard/view_inspection.html', {'inspection': inspection})


