
from django.urls import path, include
from . import views
from products.views import ProductDetailAPIView

urlpatterns = [
    path('', views.api_home),
    path('add_product/', views.api_product_create),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]