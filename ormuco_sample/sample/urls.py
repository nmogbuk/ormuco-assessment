from django.contrib.auth import views as auth_views
from django.urls import path

from sample import views

app_name = 'sample'
urlpatterns = [
    path('', views.index, name='index'),
]