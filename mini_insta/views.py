# File: views.py
# Author: Matthew Hepburn, 9/24/2026
# Description: views file that renders pages for insta views

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post
from .forms import CreatePostForm
from django.urls import reverse

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

class PostDetailView(DetailView):
    '''Define a view vlass to show a detailed post'''

    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

class CreatePostView(CreateView):
    '''View to handle creation of a new Post
    (1) display html form to user (GET)
    (2) process the form submission and store the new Post object (POST)
    '''

    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    def form_valid(self, form):
        '''handles the form submission and saves the new object to db
        we need to add foreign key of the user to the post object before saving to db
        '''

        #retrieve the pk from the url pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        #attach this article to the comment
        form.instance.profile = profile

        #delegate work to superclass method
        return super().form_valid(form)

    # def get_success_url(self):
    #     '''provide a url to redirect after making a new post'''
    #     pk = self.kwargs['pk']
    #     return reverse('show_post',kwargs={'pk':pk})

    def get_context_data(self):
        '''add profile thats making a post to context'''
        context = super().get_context_data()

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile
        return context
