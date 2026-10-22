# File: views.py
# Author: Matthew Hepburn, 9/24/2026
# Description: views file that renders pages for insta views

from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


class InstaLRM(LoginRequiredMixin):
    '''subclass for repetitive methods of login required mixin'''
    def get_login_url(self):
        '''method to take user to login page if not signed it'''
        return reverse('login')

    def get_user_profile(self):
        '''find the profile of a logged in user'''
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return profile

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

class UserProfileView(InstaLRM, ProfileDetailView):
    '''Class to show the users profile'''
    def get_object(self, queryset = ...):
        '''get the signed in user profile as the object'''
        return self.get_user_profile()

class PostDetailView(DetailView):
    '''Define a view vlass to show a detailed post'''

    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

class CreatePostView(InstaLRM, CreateView):
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
        # pk = self.kwargs['pk']
        # profile = Profile.objects.get(pk=pk)
        #attach this article to the comment
        # form.instance.profile = profile

        # retrieve the user from request
        form.instance.profile = self.get_user_profile()

        # make the post object so we can attach the photos after
        response = super().form_valid(form)

        files = self.request.FILES.getlist('files') #iterate through all photo files from POST
        for file in files:
            Photo.objects.create(image_file=file,post = self.object)

        #delegate work to superclass method
        return response

    def get_success_url(self):
        '''redirect to the post that was just created'''
        return reverse('show_post', kwargs={'pk': self.object.pk})

    def get_context_data(self):
        '''add profile thats making a post to context'''
        context = super().get_context_data()

        profile = self.get_user_profile()

        context['profile'] = profile
        return context


class UpdateProfileView(InstaLRM, UpdateView):
    '''View to handle updating an existing profile's attributes'''

    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'
    model = Profile

    def get_context_data(self):
        '''add profile being updated to context'''
        context = super().get_context_data()

        profile = self.get_user_profile()

        context['profile'] = profile

        return context

    def get_object(self, queryset = ...):
            '''get the signed in user profile as the object'''
            return self.get_user_profile()

class UpdatePostView(UpdateView):
    '''View to handle updating an existing post's attributes'''

    form_class = UpdatePostForm
    template_name = 'mini_insta/update_post_form.html'
    model = Post

    def get_context_data(self):
        '''add post to context'''
        context = super().get_context_data()

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        context['post'] = post
        return context

class DeletePostView(DeleteView):
    '''View class to delete a post'''

    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_context_data(self, **kwargs):
        '''add the post and profile to context'''
        context = super().get_context_data(**kwargs) # added **kwargs to fix an error

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = post.profile

        context['post'] = post
        context['profile'] = profile

        return context

    def get_success_url(self):
        '''return to the profile page after deletion'''
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = post.profile

        return reverse('show_profile', kwargs={'pk' : profile.pk})


class ShowFollowersDetailView(DetailView):
    '''view to show all followers for one account'''
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
    '''view to show all following for one account'''
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'

class ShowFeedView(InstaLRM, DetailView):
    '''view to show the post feed for a user'''
    model = Profile
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'profile'

    def get_object(self, queryset = ...):
        '''get the signed in user profile as the object'''
        return self.get_user_profile()

class SearchView(InstaLRM, ListView):
    '''View to input a search and display results'''
    template_name = 'mini_insta/search_results.html'

    def dispatch(self, request, *args, **kwargs):
        '''handles dispatch for requests'''
        if 'query' in request.GET:
            return super().dispatch(request, *args, **kwargs)
        else:
            if request.user.is_authenticated:
                profile = self.get_user_profile()
                return render(request,template_name='mini_insta/search.html',context={'profile':profile})
            else:
                return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''returns all posts that match the query'''
        query = self.request.GET.get('query')
        return Post.objects.filter(caption__contains=query)

    def get_context_data(self, **kwargs):
        '''adds the profile making search, and query + results to the context if they exist'''
        context = super().get_context_data(**kwargs)

        profile = self.get_user_profile()
        context['profile'] = profile

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            context['query'] = query

            context['posts'] = self.get_queryset()

            # get queryset of each match
            userMatch = Profile.objects.filter(username__contains=query)
            displayMatch = Profile.objects.filter(display_name__contains=query)
            bioMatch = Profile.objects.filter(bio_text__contains=query)

            # or them together and filter duplicates
            profiles = userMatch | displayMatch | bioMatch
            profiles = profiles.distinct()

            context['profiles'] = profiles

        return context


class CreateProfileView(CreateView):

    template_name = 'mini_insta/create_profile_form.html'
    form_class = CreateProfileForm
    model = Profile

    def get_context_data(self, **kwargs):
        '''add the usercreationform to context'''
        context = super().get_context_data(**kwargs)
        context['ucform'] = UserCreationForm

        return context

    def form_valid(self, form):
        '''connect a newly created profile to user'''

        # reconstruct the user from post
        userform = UserCreationForm(self.request.POST)
        if userform.is_valid():
            user = userform.save()
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

            # add the user username to profile username so they match
            form.instance.username = self.request.POST.get('username')

            # add user to profile
            form.instance.user = user

            return super().form_valid(form)
        else:
            return self.form_invalid(form)


    def get_success_url(self):
        return reverse('show_user_profile')


class NewLikeView(TemplateView):
    '''class to make a new like'''
    def dispatch(self, request, *args, **kwargs):
        '''make the new like'''
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        profile = Profile.objects.get(user=self.request.user)

        newLike = Like.objects.create(post=post, profile=profile)

        # redirect to same page so the url stays consistent
        return redirect('show_post', pk=pk)

class DeleteLikeView(TemplateView):
    '''class to remove a like'''
    def dispatch(self, request, *args, **kwargs):
        '''remove the like'''
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        profile = Profile.objects.get(user=self.request.user)

        like = Like.objects.get(post=post,profile=profile)
        like.delete()

         # redirect to same page so the url stays consistent
        return redirect('show_post', pk=pk)

class NewFollowView(TemplateView):
    '''class to make a new follow'''
    def dispatch(self, request, *args, **kwargs):
        '''make the new follow'''
        pk = self.kwargs.get('pk')
        profile = Profile.objects.get(pk=pk)

        follower_profile = self.request.user.profile

        newFollow = Follow.objects.create(profile=profile,follower_profile=follower_profile)


         # redirect to same page so the url stays consistent
        return redirect('show_profile', pk=pk)

class DeleteFollowView(TemplateView):
    '''class to remove a follow'''
    def dispatch(self, request, *args, **kwargs):
        '''remove the follow'''
        pk = self.kwargs.get('pk')
        profile = Profile.objects.get(pk=pk)

        follower_profile = self.request.user.profile

        oldFollow = Follow.objects.get(profile=profile,follower_profile=follower_profile)
        oldFollow.delete()

         # redirect to same page so the url stays consistent
        return redirect('show_profile', pk=pk)