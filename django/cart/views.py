from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Cake
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart' : cart
    }
    return render(request, 'cart/detail.html', context)

def cart_add(request, cake_id):
    cart = Cart(request)
    cake = get_object_or_404(Cake, id = cake_id)
    cart.add(cake=cake)
    return redirect('cart_detail')

def cart_remove(request, cake_id):
    cart = Cart(request)
    cake = get_object_or_404(Cake, id = cake_id)
    cart.remove(cake=cake)
    return redirect('cart_detail')

