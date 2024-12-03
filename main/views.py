from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
# from main.models import 


def home_page(request):
    return render(request,'home_page.html',) 
# Create your views here.
