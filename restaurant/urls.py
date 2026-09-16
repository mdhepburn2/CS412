from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'main', views.main, name='main_page'),
    path(r'', views.main, name='main_page'),
    path(r'order', views.order, name='order_page'),
    path(r'confirmation', views.submit, name='confirmation'),
]