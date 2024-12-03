from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category
from django.shortcuts import render, get_object_or_404

class ProductListView(ListView):
    model = Product
    template_name = 'products.html' 
    context_object_name = 'products' 
    
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        qs = Product.objects.filter(category_id=category_id)
        return qs
    
class ProductDetailView(DetailView):
    model = Product
    slug_field = 'id'
    slug_url_kwarg = 'product_id'
    template_name = 'products_details.html'

