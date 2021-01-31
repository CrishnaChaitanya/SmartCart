from django.contrib import admin
from django.urls import path
from . import views

from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contactUs/', views.contactUs, name='blog-contactus'),
    path('loginPage/', views.loginPage, name='blog-login'),
    path('register/', views.register, name='blog-register'),
    path('shop/', views.shop, name='blog-shop'),
    path('logout/', views.loginPage, name="logout"),
    path('product/', views.product, name='blog-product'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
