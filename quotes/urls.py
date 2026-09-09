from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.quote, name='quote_page'),
    path(r'quote', views.quote, name='quote_page')
]