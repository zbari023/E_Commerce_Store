from .models import Cart


def get_cart_data(request):
    cart = Cart.objects.get(user=request.user)
    return {'cart_data':cart}