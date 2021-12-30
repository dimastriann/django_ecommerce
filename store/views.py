from django.shortcuts import render

from .models import *


# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'store/store.html', context)


def cart(request):
    return render(request, 'store/cart.html', {"range": range(1,6)})


def checkout(request):
    return render(request, 'store/checkout.html')