from django.conf.urls import url

from . import views


app_name= 'posts'
urlpatterns = [
    url(r'^$', views.index, namespace='index'),
    url(r'^(?P<post_id>[0-9]+)$', views.detail, namespace='detail'),
]
