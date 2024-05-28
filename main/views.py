from django.http import HttpResponse
from django.shortcuts import render
from main.models import plots

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