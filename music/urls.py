from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # url(r'^login/$', views.LoginView.as_view(), name='login'),
    # url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout,{'next_page': 'music:index'}, name='logout'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url('^', include('django.contrib.auth.urls')),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    #url(r'^accounts/', include('django.contrib.auth.urls')),


    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),
    url(r'album/(?P<pk>[0-9]+)/$',
        views.AlbumUpdate.as_view(), name='album_update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$',
        views.AlbumDelete.as_view(), name='album_delete'),


    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',
        views.DetailView.as_view(), name='favorite'),
]
