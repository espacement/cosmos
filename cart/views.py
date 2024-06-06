from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import plots
from .forms import AddToCartForm

@require_POST
def add_to_cart(request):
    form = AddToCartForm(request.POST)
    if form.is_valid():
        product_id = str(form.cleaned_data['product_id'])
        quantity = form.cleaned_data['quantity']
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        request.session['cart'] = cart
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    products = plots.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
            'total_price': product.price * cart[str(product.id)]
        })
    total_amount = sum(item['total_price'] for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_amount': total_amount})

@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart:cart_detail')