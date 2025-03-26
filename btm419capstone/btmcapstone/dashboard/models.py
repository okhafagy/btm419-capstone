from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10000, decimal_places=1)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name