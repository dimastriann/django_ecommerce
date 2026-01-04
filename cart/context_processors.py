from .models import Cart, CartItem
from .views import _cart_id


def cart_counter(request):
    item_count = 0
    if "admin" in request.path:
        return {}
    try:
        if request.user.is_authenticated:
            cart = (
                Cart.objects.filter(user=request.user).order_by("-date_added").first()
            )
        else:
            cart = Cart.objects.filter(cart_id=_cart_id(request)).first()

        if cart:
            cart_items = CartItem.objects.all().filter(cart=cart)
            for cart_item in cart_items:
                item_count += cart_item.quantity
    except Exception:
        item_count = 0
    return dict(counter=item_count)
