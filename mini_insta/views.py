# File: views.py
# Author: Matthew Hepburn, 9/24/2026
# Description: views file that renders pages for insta views

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.
class ProfileListView(ListView):
    '''Define a view class to show all insta profiles'''

    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    '''Define a view class to show a detailed insta profile'''

    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'