from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE6bVUYQ63xL31ah8UOXlkdSgCw8ehULcn_gEsEg85pA&s=10',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY1N3QxpuTljKqbDH4VMuuQvJm1y4afmjprmI6XOiI5A&s=10',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXiP5APPh1lqHit0UJtT37BjnHkghTT-akc8Xcyv42_w&s=10',
    'https://upload.wikimedia.org/wikipedia/commons/e/e3/Frank_Ocean_2022_Blonded.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original',
    'https://bi.org/wp-content/uploads/2019/10/featured-famous-bi-frank-ocean-1024x1024.jpg',

]

quotes = [
    '"Many college students have gone to college"',
    '"Work hard in silence, let your success be your noise"',
    '"Living so the last night feels like a past life"',
    '"Don\'t confuse my personality with my attitude. My personality is who I am, and my attitude depends on who you are"',
    '"When you\'re happy, you enjoy the music, but when you\'re sad, you understand the lyrics"',
]

# Create your views here.

def quote(request):
    """
    process request for quote page
    img and quote context variables pick a random image/quote from the global arrays
    """
    template_name = "quotes/quote.html"

    context = {
        "img" : images[random.randint(0,len(images) - 1)],
        "quote" : quotes[random.randint(0,len(quotes) - 1)],
    }

    return render(request, template_name, context)

def about(request):
    """process request for about page"""
    template_name = "quotes/about.html"

    return render(request, template_name)

def show_all(request):
    """
    process request for show_all page
    passes the entire arrays as context so django can loop in html
    """
    template_name = "quotes/show_all.html"

    context = {
        "quotes" : quotes,
        "images" : images,
    }

    return render(request, template_name, context)