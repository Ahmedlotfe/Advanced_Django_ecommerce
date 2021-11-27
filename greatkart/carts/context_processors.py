from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from .views import _cart_id


def get_items(request):
    counter = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = get_object_or_404(Cart, cart_id=_cart_id(request))
            items = CartItem.objects.filter(cart=cart)
            for item in items:
                counter += item.quantity
        except Cart.DoesNotExist:
            counter = 0

    return dict(counter=counter)
