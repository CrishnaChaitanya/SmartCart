from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contactUs/', views.contactUs, name='blog-contactus'),
    path('loginPage/', views.loginPage, name='blog-login'),
    path('register/', views.register, name='blog-register'),
    path('shop/', views.shop, name='blog-shop'),
    path('logout/', views.loginPage, name="logout"),
    path('product/', views.product, name='blog-product'),

]
