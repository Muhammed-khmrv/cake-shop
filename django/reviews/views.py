from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Cake
from .forms import ReviewForm
from .models import Review


def add_review(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.cake_id = cake.id
            review.save(using='reviews_db')
            return redirect('cake_detail', slug=cake.slug)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'cake': cake
    })