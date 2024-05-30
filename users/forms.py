from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'placeholder': 'Введите логин',
                                    }),)
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                      'placeholder': 'Введите пароль',
                                      }),)
    class Meta:
        model = AbstractUser
        fields = ['username', 'password']