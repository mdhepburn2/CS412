# File: urls.py
# Author: Matthew Hepburn, 9/24/2026
# Description: urls file that tells http request what views file to use for mini_insta

from django.urls import path
from django.conf import settings
from . import views
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path(r'', ProfileListView.as_view(), name='show_all_profiles'),
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
]