from django import forms
from .models import InventoryLog

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = InventoryLog
        fields = ['purchase_id', 'inventory_id', 'quantity', 'per_unit_value', 'expected_delivery_date', 'actual_delivery_date']
        labels = {
            'inventory_id': 'Inventory Name',  
            'purchase_id': 'Purchase ID',
            'quantity': 'Quantity',
            'per_unit_value': 'Price Per Unit',
            'expected_delivery_date': 'Order Date',
            'actual_delivery_date': 'Delivery Date',
        }
        widgets = {
            'expected_delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }
