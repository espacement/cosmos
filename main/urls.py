from django.urls import path
from main import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('add_to_cart/<int:plot_id>/', views.add_to_cart, name='add_to_cart'),  # Добавьте эту строку
    path('cart_detail/', views.cart_detail, name='cart_detail'),
]

