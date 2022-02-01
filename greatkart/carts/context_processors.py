from .models import Cart, CartItem
from .views import _cart_id


def get_items(request):
    counter = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            if request.user.is_authenticated:
                items = CartItem.objects.filter(user=request.user)
            else:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                items = CartItem.objects.filter(cart=cart)
            for item in items:
                counter += item.quantity
        except Cart.DoesNotExist:
            counter = 0

    return {'counter': counter}
