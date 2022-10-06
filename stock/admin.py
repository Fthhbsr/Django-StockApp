from django.contrib import admin

from .models import Brand, Category, Firm, Product, TransactionStock

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(TransactionStock)

