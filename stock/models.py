from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.category_name}'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand_name}'

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    stock = models.IntegerField(null = True)

    def __str__(self):
        return f'{self.product_name}'


class Firm(models.Model):
    firm_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firm_name}'


class TransactionStock(models.Model):
    TRANSACTION = [ # choices = IN or OUT
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    ]
    user = models.ForeignKey(User, related_name="transaction_owner", on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, related_name="transaction_firm", on_delete=models.CASCADE)
    transaction = models.CharField(max_length=3, choices= TRANSACTION)
    product = models.ForeignKey(Product, related_name="transaction_product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.product} - {self.transaction}'

    # def price_total_calc(self):
    #     self.price_total = self.price * self.quantity
    #     return self.price_total

