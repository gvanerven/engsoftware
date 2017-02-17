from django.conf.urls import url
from django.contrib import admin
from mcritica import views

urlpatterns = [
    url(r'^$', views.index, name='mcritica/index'),
]