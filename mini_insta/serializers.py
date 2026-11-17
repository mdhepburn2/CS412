# File: serializers.py
# Author: Matthew Hepburn, 11/16/2026
# Description: holds serializer information for the mini insta api

from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    '''A serializer for the profile model'''
    pfp_url = serializers.URLField(source='get_pfp_url', read_only=True)
    num_followers = serializers.IntegerField(source='get_num_followers')
    num_following = serializers.IntegerField(source='get_num_following')
    num_posts = serializers.IntegerField(source='get_num_posts')
    # all_posts = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'username',
            'display_name',
            'pfp_url',
            'bio_text',
            'join_date',
            'user',
            # 'all_posts',
            'num_followers',
            'num_following',
            'num_posts',
            'pk',
        ]

    # def get_all_posts(self, obj):
    #     return PostSerializer(obj.get_all_posts(), many=True).data

class PostSerializer(serializers.ModelSerializer):
    '''A serializer for the post model'''
    all_photos = serializers.SerializerMethodField()
    first_photo = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'profile',
            'timestamp',
            'caption',
            'all_photos',
            'first_photo',
            'pk',
        ]

    def get_all_photos(self, obj):
        return PhotoSerializer(obj.get_all_photos(), many=True).data

    def get_first_photo(self, obj):
        return PhotoSerializer(obj.get_first_photo()).data


class PhotoSerializer(serializers.ModelSerializer):
    '''A serializer for the photo model'''
    url = serializers.URLField(source='get_image_url', read_only=True)

    class Meta:
        model = Photo
        fields = [
            'post',
            'timestamp',
            'url',
        ]