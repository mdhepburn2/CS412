from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE6bVUYQ63xL31ah8UOXlkdSgCw8ehULcn_gEsEg85pA&s=10',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY1N3QxpuTljKqbDH4VMuuQvJm1y4afmjprmI6XOiI5A&s=10',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXiP5APPh1lqHit0UJtT37BjnHkghTT-akc8Xcyv42_w&s=10',
]

quotes = [
    '"Many college students have gone to college"',
    '"Work hard in silence, let your success be your noise"',
    '"Living so the last night feels like a past life"',
]

# Create your views here.

def quote(request):
    template_name = "quotes/quote.html"

    context = {
        "img" : images[random.randint(0,len(images) - 1)],
        "quote" : quotes[random.randint(0,len(quotes) - 1)],
    }

    return render(request, template_name, context)

def about(request):
    template_name = "quotes/about.html"

    return render(request, template_name)

def show_all(request):
    template_name = "quotes/show_all.html"

    context = {
        "quotes" : quotes,
        "images" : images,
    }

    return render(request, template_name, context)