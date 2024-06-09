from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        item_count = cart.cartitem_set.count()
    else:
        item_count = 0
    return {'cart_item_count': item_count}