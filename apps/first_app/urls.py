from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^vote$', views.vote),
    url(r'^view_votes$', views.view_votes),
    url(r'^votes$', views.see_votes),
    url(r'^add_person$', views.add_person),
    url(r'^reset_votes$', views.reset_votes),
    url(r'^delete_database$', views.delete_database),
    url(r'^goinput$', views.goinput),
]
