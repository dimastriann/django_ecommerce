from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart, CartItem
from cart.views import _cart_id


def order_create(request):
    try:
        if request.user.is_authenticated:
            cart = (
                Cart.objects.filter(user=request.user).order_by("-date_added").first()
            )
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))

        if cart:
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        else:
            cart_items = []
    except Exception:
        cart_items = []

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )
            # Clear items from cart
            if cart:
                cart_items.delete()

            return render(request, "orders/created.html", {"order": order})
    else:
        form = OrderCreateForm()

    return render(
        request, "orders/create.html", {"cart_items": cart_items, "form": form}
    )
