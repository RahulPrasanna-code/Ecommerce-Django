from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='products_page'),
    path('<product_id>',views.product_detail_view,name='product_detail_view'),
]
