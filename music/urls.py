from django.conf.urls import include, url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album.add/$', views.AlbumCreate.as_view(), name='album_add'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',
        views.DetailView.as_view(), name='favorite'),
]
