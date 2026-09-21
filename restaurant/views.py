from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random


specials = [
    'Penne alla Vodka',
    'Cacio e Pepe',
    'Spaghetti alla Carbonara',
]

prices = {
    'pizza': 12,
    'lasagna': 13,
    'chicken_parmesan': 16,
    'tagliatelle_bolognese': 15,
    'Cheese': 0,
    'Pepperoni': 1,
    'Sausage': 1,
    'Barbecue Chicken': 3,
    'special' : 20,
}

menu = {
    'pizza': 'Pizza',
    'lasagna': 'Lasagna',
    'chicken_parmesan': 'Chicken Parmesan',
    'tagliatelle_bolognese': 'Tagliatelle Bolognese',
    'special' : 'Special',
}

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

def confirmation(request):
    '''process form submission and generate result'''
    template_name = "restaurant/confirmation.html"

    if request.POST:
        print(request.POST)
        #collect customer info
        context = {
            'name': request.POST.get('name'),
            'email' : request.POST.get('email'),
            'phone' : request.POST.get('phone'),
        }
        if request.POST.get('special_instructions') == '':
            context['special_instructions'] = 'None'
        else:
            context['special_instructions'] = request.POST.get['special_instructions']

        #sum up total cost and add to receipt
        receipt = []
        sum = 0
        for key in request.POST:
            if prices.get(key) != None:
                sum += prices[key]
                if key == 'pizza':
                    receipt.append(request.POST.get('pizza_topping') + ' Pizza')
                else:
                    receipt.append(menu[key])
        sum += prices.get(request.POST.get('pizza_topping'))
        context['total'] = sum
        context['receipt'] = receipt

        # calculate ready time
        current = time.time()
        context['current'] = time.ctime(current)
        ready = time.ctime(current + (random.randint(30,60) * 60))
        context['ready'] = ready
    

    return render(request, template_name, context)