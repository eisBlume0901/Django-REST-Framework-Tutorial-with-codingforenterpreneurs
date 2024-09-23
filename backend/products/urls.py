from django.urls import path
from .views import ProductDetailAPIView

urlpatterns = [
    path('<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'), #lookup_field should be the same as the one in the view
]