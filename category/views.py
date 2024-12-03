from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Категории")

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog.html'


    def catalog_page(request):
     if request.method == 'GET':
         object_list = Category.objects.all()
         return render(request, 'catalog.html', { 'object_list': object_list })
    
     return HttpResponse('')



# Create your views here.
