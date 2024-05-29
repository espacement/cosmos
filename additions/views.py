from django.shortcuts import render
from additions.models import news, gallery
# Create your views here.


def galler(request):
    galler = gallery.objects.all()
    context = {
        "title": "Галерея",
        "gallery": galler,
    }
    return render(request, "additions/photos.html", context)


def public(request):
    new = news.objects.all()
    context = {
        "title": "Интересное",
        "news": new,
    }
    return render(request, "additions/public.html", context)