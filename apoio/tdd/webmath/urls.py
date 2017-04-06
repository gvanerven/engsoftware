from django.conf.urls import url

from webmath import views

urlpatterns = [

    url(r'^$', views.index, name='webmath'),
    url(r'^raiz/(?P<numero>\d+)$', views.raiz, name='webmath/raiz'),

]