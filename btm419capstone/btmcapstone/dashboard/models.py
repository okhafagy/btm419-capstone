from django.db import models

class Inventory(models.Model):
    inventory_id = models.IntegerField(unique=True)
    count = models.IntegerField()
    
    def __str__(self):
        return f"Inventory ID: {self.inventory_id}, Count: {self.count}"    
    
class InventoryLog(models.Model):
    purchase_id = models.IntegerField()
    inventory_id = models.CharField(max_length=255)
    quantity = models.IntegerField()
    per_unit_value = models.DecimalField(max_digits=10, decimal_places=2)
    expected_delivery_date = models.DateField()
    actual_delivery_date = models.DateField()
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00) 
    
    def __str__(self):
        return f"Purchase ID: {self.purchase_id}, Inventory ID: {self.inventory_id}, Quantity: {self.quantity}, Per Unit Value: {self.per_unit_value}, Expected Delivery Date: {self.expected_delivery_date}, Actual Delivery Date: {self.actual_delivery_date}"
    

class Complaint(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(default='')
    organization = models.CharField(max_length=100, default='')
    item = models.CharField(max_length=100, default='')
    text = models.TextField()
    sale_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"Complaint {self.id}, {self.name}"
    
class Inspection(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default='')
    car_model = models.CharField(max_length=100, default='')
    claim_id = models.CharField(max_length=100, default='')
    warranty_id = models.CharField(max_length=100, default='')
    dealership = models.CharField(max_length=100, default='')
    VIN = models.CharField(max_length=100, default='')
    estimated_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Inspection {self.inspection_id}, {self.inspector_name}"

class Sale(models.Model):
    sale_number = models.CharField(max_length=100)
    dealership = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expected_delivery_date = models.DateField()
    actual_delivery_date = models.DateField()

    def __str__(self):
        return f"Sale Number: {self.sale_number}, Dealership: {self.dealership}, Product: {self.product}, Quantity: {self.quantity}, Expected Delivery Date: {self.expected_delivery_date}, Actual Delivery Date: {self.actual_delivery_date}"  
    