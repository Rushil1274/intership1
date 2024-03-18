from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(upload_to='uploads/images/', null=False, blank=False)
    category = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

