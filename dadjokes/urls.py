# File: urls.py
# Author: Matthew Hepburn, 11/11/2026
# Description: urls file that tells http request what views file to use for dadjokes


from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    # web app urls
    path('', views.random, name='random'),
    path('random', views.random, name='random'),
    path('jokes', JokeListView.as_view(), name='all_jokes'),
    path('joke/<int:pk>', JokeDetailView.as_view(), name='show_joke'),
    path('pictures', PictureListView.as_view(), name='all_pictures'),
    path('picture/<int:pk>', PictureDetailView.as_view(), name='show_picture'),

    # api urls
    path('api/', RandomJokeAPIView.as_view()),
    path('api/random/', RandomJokeAPIView.as_view()),
    path('api/jokes/', JokeListAPIView.as_view()),
    path('api/joke/<int:pk>/', JokeDetailAPIView.as_view()),
    path('api/pictures/', PictureListAPIView.as_view()),
    path('api/picture/<int:pk>/', PictureDetailAPIView.as_view()),
    path('api/random_picture/', RandomPictureView.as_view()),
]