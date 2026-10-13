# File: urls.py
# Author: Matthew Hepburn, 9/24/2026
# Description: urls file that tells http request what views file to use for mini_insta

from django.urls import path
from django.conf import settings
from . import views
from .views import *
urlpatterns = [
    path(r'', ProfileListView.as_view(), name='show_all_profiles'),
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
    path(r'post/<int:pk>', PostDetailView.as_view(), name = 'show_post'),
    path(r'profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
    path(r'profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path(r'post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path(r'post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]