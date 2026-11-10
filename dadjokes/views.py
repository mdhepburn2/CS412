from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView
from rest_framework import generics
from .serializers import *
import random as rand

# Create your views here.
def random(request):
    '''View to show a random joke and picture'''
    joke = rand.choice(Joke.objects.all())
    picture = rand.choice(Picture.objects.all())
    template_name = 'dadjokes/show_random.html'

    return render(request, template_name, {'joke': joke, 'picture': picture})

class JokeListView(ListView):
    '''Show all jokes'''
    template_name = 'dadjokes/all_jokes.html'
    model = Joke
    context_object_name = 'jokes'

class JokeDetailView(DetailView):
    '''Show one specific joke'''
    template_name = 'dadjokes/show_joke.html'
    model = Joke
    context_object_name = 'joke'

    def get_object(self, queryset = ...):
        return Joke.objects.get(pk=self.kwargs['pk'])

class PictureListView(ListView):
    '''Show all pictures'''
    template_name = 'dadjokes/all_pictures.html'
    model = Picture
    context_object_name = 'pictures'

class PictureDetailView(DetailView):
    '''Show one specific picture'''
    template_name = 'dadjokes/show_picture.html'
    model = Picture
    context_object_name = 'picture'

    def get_object(self, queryset = ...):
        return Picture.objects.get(pk=self.kwargs['pk'])


##
### API views
##

class RandomJokeAPIView(generics.RetrieveAPIView):
    '''API view to return a random joke'''
    queryset = rand.choice(Joke.objects.all())
    serializer_class = JokeSerializer

    def get_object(self):
        '''override get object to show the random selection'''
        return self.queryset

class JokeListAPIView(generics.ListCreateAPIView):
    '''An api view to show all jokes and to create a joke'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Api view to show a specific joke'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class RandomPictureView(generics.RetrieveAPIView):
    '''API view to return a random picture'''
    queryset = rand.choice(Picture.objects.all())
    serializer_class = PictureSerializer

    def get_object(self):
        '''override get object to show the random selection'''
        return self.queryset

class PictureListAPIView(generics.ListCreateAPIView):
    '''api view to show all pictures'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''api view to show a specific picture'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer