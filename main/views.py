from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import plots
from cart.forms import AddToCartForm

# Create your views here.
def index(request):
    plot = plots.objects.all()
    form = AddToCartForm()
    cart = request.session.get('cart', {})
    cart_items = [{'id': key, 'quantity': value} for key, value in cart.items()]
    context = {
        'title': 'CosmoGround',
        'plots': plot,
        'form': form,
        'cart_items': cart_items,
    }
    return render(request, 'main/index.html', context)

def add_to_cart(request):
    form = AddToCartForm(request.POST)
    if form.is_valid():
        product_id = form.cleaned_data['product_id']
        quantity = form.cleaned_data['quantity']
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        request.session['cart'] = cart
    return redirect('main:index')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('main:index')


def faq(request):
    context = {
        'title': 'FAQ',
    }
    return render(request, 'main/faq.html', context)