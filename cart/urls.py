from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/add', views.add_to_cart, name='add-to-cart'),
    path('', views.cart_list_view, name='cart-page'),
]
