from django.conf.urls import include, url
from learn import views



urlpatterns = [
    url(r'^learn/', views.home),
    url(r'^about/', views.about),
]