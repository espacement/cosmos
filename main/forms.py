from django import forms
from .models import CartItem
from .models import plots

class AddToCartForm(forms.ModelForm):
    plot = forms.ModelChoiceField(queryset=plots.objects.all(), widget=forms.HiddenInput())
    quantity = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    class Meta:
        model = CartItem
        fields = ['plot', 'quantity']