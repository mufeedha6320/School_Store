from django.urls import path
from . import views

app_name = "storeapp"

urlpatterns = [
    path('',views.demo,name='demo'),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/order/',views.order, name='order'),
    path('logout/', views.logout, name='logout'),
]
