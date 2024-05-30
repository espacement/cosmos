from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

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
        model = User
        fields = ['username', 'password']



class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя',}),)
    
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию',}),)
    
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={ 'placeholder': 'Введите логин',}),)
    
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={ 'placeholder': 'Введите email *youremail@example.com', }),)
    
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль',}),)
    
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль',}),)
    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',]