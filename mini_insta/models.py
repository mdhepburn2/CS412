# File: models.py
# Author: Matthew Hepburn, 9/24/2026
# Description: holds the data for mini insta such as user profiles

from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Holds the data for a user profile'''

    #data attributes for a profile
    username = models.TextField()
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField()
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of a profile'''
        return f'{self.display_name} ({self.username})'

    def get_all_posts(self):
            '''return the queryset of all posts for a user'''
            return Post.objects.filter(profile=self).order_by('-timestamp')


class Post(models.Model):
    '''Holds the data for a user post and references photos from db'''

    #data attributes for a post
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of a post'''
        return f'Post by {self.profile}: ({self.caption})'

    def get_all_photos(self):
        '''return queryset of all photos attached to a post'''

        return Photo.objects.filter(post=self)

    def get_first_photo(self):
         '''return only the first photo for the not detailed view'''

         return Photo.objects.filter(post=self).first()


class Photo(models.Model):
    '''Holds the data for a photo object'''

    #data attributes for a photo
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of a photo'''
        return f'Photo on {self.post} ({self.image_url})'
    