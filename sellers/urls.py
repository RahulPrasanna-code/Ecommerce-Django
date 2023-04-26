from django.urls import path
from . import views


urlpatterns = [
    path('products',views.seller_dashboard,name='seller_dashboard'),
    path('',views.seller_intro_page,name='seller_intro_page'),
    path('login',views.seller_login,name='seller_login'),
    path('products/<product_id>',views.seller_detail_view,name='seller_detail_view'),
    path('delete',views.delete_products,name='delete_products'),
    path('create',views.create_product,name='create_product'),
    path('update/<product_id>',views.update_product_view,name='update_product'),
    path('updatedata',views.update_product,name='update_product_data')
]
