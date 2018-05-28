from django.urls import include, path
from learn import views




urlpatterns = [
        path('learn/<int:year>/', views.about),
        path('learn/test', views.current_datetime)
]