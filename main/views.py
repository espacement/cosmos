from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import plots, Cart, CartItem, Order, OrderItem
from .forms import AddToCartForm, CheckoutForm
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

@login_required
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


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Товар удален из корзины!')
    return redirect('main:cart_detail')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.cartitem_set.exists():
        messages.error(request, 'Ваша корзина пуста')
        return redirect('main:cart_detail')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                total_cost=cart.get_total_cost()
            )
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(
                    order=order,
                    plot=item.plot,
                    quantity=item.quantity
                )
            cart.cartitem_set.all().delete()
            messages.success(request, 'Покупка успешно завершена!')
            return redirect('main:order_success')
    else:
        form = CheckoutForm()
    
    return render(request, 'main/checkout.html', {'form': form})

@login_required
def order_success(request):
    return render(request, 'main/order_success.html')

