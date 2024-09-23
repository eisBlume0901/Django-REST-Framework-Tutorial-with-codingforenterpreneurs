
from django.urls import path
from . import views
urlpatterns = [
    path('', views.api_home),
    path('add_product/', views.api_product_create),
]