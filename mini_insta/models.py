# File: models.py
# Author: Matthew Hepburn, 9/24/2026
# Description: holds the data for mini insta such as user profiles

from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Holds the data for a user profile'''

    username = models.TextField()
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField()
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of a profile'''
        return f'{self.display_name} ({self.username})'
    