# File: urls.py
# Author: Matthew Hepburn (mhepburn@bu.edu), 10/27/2026
# Description: URL patterns for the voter analytics app. Maps the home and voter list
#   pages, the individual voter detail page, and the graphs page to their views.

from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', VotersListView.as_view(), name='home'),
    path('voters', VotersListView.as_view(), name='voters_list'),
    path('voter/<int:pk>', VoterDetailView.as_view(), name='show_voter'),
    path('graphs', GraphView.as_view(), name='graphs')
]