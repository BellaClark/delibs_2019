from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^vote$', views.vote),
    url(r'^view_votes$', views.view_votes),
    url(r'^votes$', views.see_votes),
]
