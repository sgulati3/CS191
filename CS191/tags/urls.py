from django.conf.urls import url

from . import views


app_name= 'tags'
urlpatterns = [
    url(r'^vote/(?P<post_id>[0-9]+)/(?P<tag_title>[A-Za-z0-9]+)$', views.vote, name='vote'),
    url(r'^unvote/(?P<post_id>[0-9]+)/(?P<tag_title>[A-Za-z0-9]+)$', views.unvote, name='unvote'),
]
