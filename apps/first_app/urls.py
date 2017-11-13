from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>[0-9]{1,4})$', views.show),
    url(r'^(?P<number>[0-9]{1,4})/edit$', views.edit),
    url(r'^(?P<number>[0-9]{1,4})/delete$', views.destroy),
]