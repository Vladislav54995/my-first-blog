from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='catalog-page'),
    path('<int:category_id>/products/', include('product.urls')),
]
