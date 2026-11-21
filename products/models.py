from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    product_image = models.CharField(max_length=255)

    discount = models.DecimalField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
   product =  models.ForeignKey(Product, on_delete=models.CASCADE)

   product_description = models.TextField(
       blank=True,
       null=True
   )