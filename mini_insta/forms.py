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