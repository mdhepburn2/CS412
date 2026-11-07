from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Model to hold a joke object'''
    text = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of a joke'''
        return f'"{self.text}" by {self.name}'

class Picture(models.Model):
    '''Model to store an image or gif for app'''
    image_url = models.URLField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of a photo'''
        return f'Photo by {self.name} at {self.timestamp}'