from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

images = [
    '',
]

quotes = [
    'lorem',
]

# Create your views here.

def quote(request):
    template_name = "quotes/quote.html"

    context = {
        "img" : images[random.randint(0,len(images) - 1)],
        "quote" : quotes[random.randint(0,len(quotes) - 1)],
    }

    return render(request, template_name, context)