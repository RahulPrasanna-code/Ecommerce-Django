from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_view,name='cart_view'),
    path('add',views.add_to_cart,name='add_to_cart'),
    path('delete',views.delete_from_cart,name='delete_from_cart')
]
