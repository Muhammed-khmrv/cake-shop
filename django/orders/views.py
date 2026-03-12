from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderCreateForm
from .models import OrderItem, Order
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            if request.user.is_authenticated:
                order.user = request.user

            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    cake=item['cake'],
                    quantity=item['quantity'],
                    price=item['price']
                )

            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/create.html', {
        'cart': cart,
        'form': form
    })


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__cake').order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})