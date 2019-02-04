from django.conf.urls import url, include
from django.contrib import admin
from landing import views

# urlpatterns =[
#     # path('', views.home, name='home'),
#      url('$', views.home, name='home'),
# ]
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.landing, name='landing')
    ]