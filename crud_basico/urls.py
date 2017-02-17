from django.conf.urls import url
from django.contrib import admin
from crud_basico import views

urlpatterns = [
    url(r'^$', views.index, name='crud_basico/index'),
]