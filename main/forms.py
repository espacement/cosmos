from django import forms
from .models import CartItem
from .models import plots

#корзина
class AddToCartForm(forms.ModelForm):
    plot = forms.ModelChoiceField(queryset=plots.objects.all(), widget=forms.HiddenInput())
    quantity = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    class Meta:
        model = CartItem
        fields = ['plot', 'quantity']

#заказ
class CheckoutForm(forms.Form):
    cardholder_name = forms.CharField(max_length=100, label="Имя держателя карты")
    card_number = forms.CharField(max_length=16, label="Номер карты", min_length=16)
    expiry_date = forms.CharField(max_length=5, label="Срок действия (MM/YY)", min_length=5)
    cvc = forms.CharField(max_length=3, label="CVC код", min_length=3)