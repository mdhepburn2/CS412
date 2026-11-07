from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''A serializer for the joke model.
    Specify which model/fields to send in the api'''

    class Meta:
        model = Joke
        fields = ['text','name','timestamp']


class PictureSerializer(serializers.ModelSerializer):
    '''A serializer for the picture model.
    Specify which model/fields to send in the api'''

    class Meta:
        model = Picture
        fields = ['image_url','name','timestamp']