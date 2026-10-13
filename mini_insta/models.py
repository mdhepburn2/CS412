# File: models.py
# Author: Matthew Hepburn, 9/24/2026
# Description: holds the data for mini insta such as user profiles

from django.db import models
from django.urls import reverse

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
        return f'{self.display_name} (@{self.username})'

    def get_all_posts(self):
            '''return the queryset of all posts for a user'''
            return Post.objects.filter(profile=self).order_by('-timestamp')

    def get_num_posts(self):
         '''return the number of posts a user has'''
         posts = Post.objects.filter(profile=self)
         return posts.count()

    def get_absolute_url(self):
         '''return the url to display one instance of this model'''
         return reverse('show_profile', kwargs={'pk' : self.pk})


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
         first = Photo.objects.filter(post=self).first()

         return first

    def get_absolute_url(self):
         '''return the url to display one instance of this model'''
         return reverse('show_post', kwargs={'pk':self.pk})


class Photo(models.Model):
    '''Holds the data for a photo object'''

    #data attributes for a photo
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(upload_to='insta_photos/',blank=True)

    def __str__(self):
        '''return a string representation of a photo'''
        if self.image_url:
            return f'Photo on {self.post} (image url)'
        elif self.image_file:
             return f'Photo on {self.post} (image upload)'
        else:
             return f'Photo on {self.post} (blank)'

    def get_image_url(self):
         '''returns the online image url or the local image url depending on where the photo is'''
         if self.image_url:
              return self.image_url
         elif self.image_file:
              return self.image_file.url
         else: # no image found image
              return 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original'
    