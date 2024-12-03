from django.urls import path
from .views import OrderCreateView, order_list_view
from . import views
urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create-order-page'),
    path('', views.order_list_view, name='orders-page'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order-details-page'),
    path('<int:order_id>/payment/create/', views.PaymentCreateView.as_view(), name='create-payment-page'),
]
