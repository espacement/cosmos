from django.shortcuts import render

# Create your views here.

def gallery(request):
    context = {
        'title': 'Галерея',
    } 
    return render(request, 'additions/photos.html', context)

def public(request):
    context = {
        'title': 'Интересное',
    }
    return render(request, 'additions/public.html', context)