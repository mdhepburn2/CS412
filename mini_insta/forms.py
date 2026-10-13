# File: forms.py
# Author: Matthew Hepburn, 10/1/2026
# Description: define the forms that we use for create/update/delete operations

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''a form to add a class to the database'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to handle updating a profile model instance'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Profile
        fields = [
            'display_name',
            'profile_image_url',
            'bio_text'
        ]

class UpdatePostForm(forms.ModelForm):
    '''A form to handle updating a post model instance'''

    class Meta:
        '''associate this form with a model from our database'''
        model = Post
        fields = [
            'caption'
        ]