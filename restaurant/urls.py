# File: urls.py
# Author: Matthew Hepburn, 9/13/2026
# Description: urls file that tells html request what views file to use for restaurant

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'main', views.main, name='main_page'),
    path(r'', views.main, name='main_page'),
    path(r'order', views.order, name='order_page'),
    path(r'confirmation', views.confirmation, name='confirmation'),
]