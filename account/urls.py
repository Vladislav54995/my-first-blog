from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name='registration-page'),
    path('register/done/', views.registration_done, name='registration-done-page'),
]