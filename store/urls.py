# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.product_list, name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('checkout/', views.order_create, name='order_create'),
]
