from django.shortcuts import render, get_object_or_404, redirect
from .models import Cake, Category
from cart.cart import Cart
from reviews.models import Review

def cake_list(request):
    cakes = Cake.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'cakes': cakes,
        'categories': categories,
    }
    return render(request, 'catalog/cake_list.html', context)

def cakes_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    cakes = Cake.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()
    context = {
        'cakes': cakes,
        'categories': categories,
        'category': category,
    }
    return render(request, 'catalog/cakes_by_category.html', context)

def cake_detail(request, slug):
    cake = get_object_or_404(Cake, slug=slug, is_available=True)

    reviews = Review.objects.using('reviews_db').filter(
        cake_id=cake.id,
    ).order_by('-created_at')

    return render(request, 'catalog/cake_detail.html', {
        'cake': cake,
        'reviews': reviews
    })