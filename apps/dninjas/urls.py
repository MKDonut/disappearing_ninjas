from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas/$', views.allturtles),
    url(r'^ninjas/(?P<id>\w+)$', views.indies)
]