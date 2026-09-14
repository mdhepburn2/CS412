from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def main(request):
    template_name = "restaurant/main.html"

    return render(request, template_name)