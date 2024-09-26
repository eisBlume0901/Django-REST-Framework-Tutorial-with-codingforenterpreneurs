from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.product_list_create_view, name='product-create'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'), #lookup_field should be the same as the one in the view
]