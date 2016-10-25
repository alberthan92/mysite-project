from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
]