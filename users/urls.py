from django.urls import path
from . import views

urlpatterns = [
    path('create',views.admin_create_buyer,name='signup'),
    path('home',views.home,name='home'),
    path('login',views.login_user,name='login')
]
