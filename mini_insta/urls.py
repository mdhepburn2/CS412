# File: urls.py
# Author: Matthew Hepburn, 9/24/2026
# Description: urls file that tells http request what views file to use for mini_insta

from django.urls import path
from django.conf import settings
from . import views
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', ProfileListView.as_view(), name='show_all_profiles'),
    path(r'profile/', UserProfileView.as_view(), name='show_user_profile'),
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
    path(r'profile/update', UpdateProfileView.as_view(), name='update_profile'),
    path(r'profile/create_post', CreatePostView.as_view(), name='create_post'),
    path(r'profile/feed', ShowFeedView.as_view(), name='show_feed'),
    path(r'profile/search', SearchView.as_view(), name='search'),
    path(r'profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),
    path(r'profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),

    path(r'profile/<int:pk>/follow', NewFollowView.as_view(), name='follow'),
    path(r'profile/<int:pk>/delete_follow', DeleteFollowView.as_view(), name='delete_follow'),

    path(r'post/<int:pk>', PostDetailView.as_view(), name = 'show_post'),
    path(r'post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path(r'post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),

    path(r'post/<int:pk>/like', NewLikeView.as_view(), name='like'),
    path(r'post/<int:pk>/delete_like', DeleteLikeView.as_view(), name='delete_like'),
    path(r'post/<int:pk>/comment', NewCommentView.as_view(), name='comment'),
    
    path(r'login/', auth_views.LoginView.as_view(template_name='mini_insta/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(next_page='show_all_profiles'), name='logout'),
    path(r'create_profile/', CreateProfileView.as_view(), name='create_profile'),

    # API urls
    path('api/profile/<int:pk>', ProfileDetailAPIView.as_view()),
    path('api/profile/<int:pk>/posts', PostListAPIView.as_view()),
    path('api/profile/<int:pk>/feed', FeedAPIView.as_view()),
    path('api/profiles', ProfileListAPIView.as_view()),

    
]