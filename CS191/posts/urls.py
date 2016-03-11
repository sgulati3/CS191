from django.conf.urls import url

from . import views


app_name= 'posts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^create$', views.create, name='create'),
    url(r'^board$', views.board, name='board')
]
