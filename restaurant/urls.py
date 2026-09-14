from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'main', views.main, name='main_page'),
    path(r'', views.main, name='main_page'),
]