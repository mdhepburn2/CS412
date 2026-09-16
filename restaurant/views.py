from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random


specials = [
    'Penne alla Vodka',
    'Cacio e Pepe',
    'Spaghetti alla Carbonara'
]

# Create your views here.
def main(request):
    '''process requests for main page'''
    template_name = "restaurant/main.html"

    return render(request, template_name)

def order(request):
    '''process requests for order page'''
    template_name = "restaurant/order.html"

    context = {
        'special': specials[random.randint(0,len(specials) - 1)]
    }

    return render(request, template_name, context)

def submit(request):
    '''process form submission and generate result'''
    template_name = "restaurant/confirmation.html"

    if request.POST:
        print(request.POST)

    return render(request, template_name)