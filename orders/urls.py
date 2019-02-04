from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns =[
    url(r'^basket_addindg/$', views.basket_addindg, name='basket_addindg'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]