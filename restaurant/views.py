from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def main(request):
    '''process requests for main page'''
    template_name = "restaurant/main.html"

    return render(request, template_name)

def order(request):
    '''process requests for order page'''
    template_name = "restaurant/order.html"

    return render(request, template_name)

def confirmation(request):
    '''process requests for confirmation page'''
    template_name = "restaurant/confirmation.html"

    return render(request, template_name)