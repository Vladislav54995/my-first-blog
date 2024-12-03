from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category',]
    list_filter = ['category',]
    search_fields = ['name__startswith',]

admin.site.register(Product, ProductAdmin)

# Register your models here.
