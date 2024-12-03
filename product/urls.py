from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-page'),
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='product-details-page'),
]
