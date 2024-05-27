from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'CosmoGround',
    }
    return render(request, 'main/index.html', context)

def faq(request):
    context = {
        'title': 'FAQ',
    }
    return render(request, 'main/faq.html', context)