from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),
    url(r'^snippets/$', views.SnippetList.as_view(),name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-detail'),
    url(r'^schema/$', schema_view),
    #url(r'^login/$', views.Login.as_view(),name='login'),
]