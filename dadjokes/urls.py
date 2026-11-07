from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', views.random, name='random'),
    path('random', views.random, name='random'),
    path('jokes', JokeListView.as_view(), name='all_jokes'),
    path('joke/<int:pk>', JokeDetailView.as_view(), name='show_joke'),
    path('pictures', PictureListView.as_view(), name='all_pictures'),
    path('picture/<int:pk>', PictureDetailView.as_view(), name='show_picture'),
]