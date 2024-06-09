from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import plots, Cart, CartItem
from .forms import AddToCartForm
from django.contrib import messages


# Create your views here.
def index(request):
    plot = plots.objects.all()
    context = {
        'title': 'CosmoGround',
        'plots': plot,
    }
    return render(request, 'main/index.html', context)

def faq(request):
    context = {
        'title': 'FAQ',
    }
    return render(request, 'main/faq.html', context)


def add_to_cart(request, plot_id):
    plot = get_object_or_404(plots, id=plot_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cart_item, created = CartItem.objects.get_or_create(cart=cart, plot=plot)
            if not created:
                cart_item.quantity += 1
            cart_item.save()
            
            
    else:
        form = AddToCartForm(initial={'plot': plot, 'quantity': 1})

    messages.info(request, f"Добавлено в корзину")
    return redirect('main:index')
    

@login_required
def cart_detail(request):
   
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'title': 'Корзина',
        'username': request.user.username,
    }
    return render(request, 'main/cart_detail.html', {'cart': cart})
    