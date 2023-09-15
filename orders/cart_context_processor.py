from .models import Cart , CartDetail


def get_cart_data(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, completed=False)
        if carts.exists():
            cart = carts.first()
        else:
            cart = Cart.objects.create(user=request.user, completed=False)

        cart_detail = CartDetail.objects.filter(cart=cart)
        return {'cart_data': cart, 'cart_detail_data': cart_detail}
    else:
        return {}