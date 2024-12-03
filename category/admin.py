from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name__startswith',]
    
admin.site.register(Category, CategoryAdmin)