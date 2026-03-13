from decimal import Decimal
from catalog.models import Cake

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, cake, quantity=1):
        cake_id = str(cake.id)
        if cake_id not in self.cart:
            self.cart[cake_id] = {
                'quantity' : 0,
                'price' : str(cake.price)
            }
        self.cart[cake_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        self.session.modified = True

    def remove(self, cake):
        cake_id = str(cake.id)
        if cake_id in self.cart:
            del self.cart[cake_id]
            self.save()
    
    def __iter__(self):
        cake_ids = self.cart.keys()
        cakes = Cake.objects.filter(id__in=cake_ids)
        cart = self.cart.copy()

        for cake in cakes:
            cart[str(cake.id)]['cake'] = cake
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        self.session['cart'] = {}
        self.save()
