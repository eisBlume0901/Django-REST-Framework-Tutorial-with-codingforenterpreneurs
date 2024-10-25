from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.product_list_create_view, name='product-create'), # To test these two class-based views, you must comment out mixins and method-based views
    path('<int:pk>/', views.product_detail_view, name='product-detail'), #lookup_field should be the same as the one in the view
#     path('', views.product_mixin_view, name='product-list'),
#     path('create/', views.product_alt_view, name='product-create'),
    path('<int:pk>/update/', views.product_update_view, name='product-update'),
    path('<int:pk>/delete/', views.product_delete_view, name='product-delete'),
    # path('<int:pk>/', views.product_alt_view, name='product-detail'),
]