from django.urls import path
from additions import views

app_name = 'additions'

urlpatterns = [
    path('public/', views.public, name='public'),
    path('gallery/', views.galler, name='gallery'),
]
