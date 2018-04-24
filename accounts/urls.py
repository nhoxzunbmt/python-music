from django.conf.urls import include, url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
