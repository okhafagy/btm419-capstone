from django import forms
from .models import Inspection 

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['name', 'car_model', 'claim_id', 'warranty_id', 'dealership', 'VIN']