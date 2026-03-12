from django.shortcuts import render
from catalog.models import Cake, Category

def home(request):
    popular_cakes = Cake.objects.filter(is_available=True)[:6]
    categories = Category.objects.all()
    context = {
        'popular_cakes': popular_cakes,
        'categories': categories,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/team.html')

def contacts(request):
    return render(request, 'core/contacts.html')