from django.shortcuts import render
from users.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def profile(request):
    # plot = plots.objects.all()
    context = {
        'title': 'Профиль',
        'plots': "ыввфы",
    }
    return render(request, 'users/profile.html', context)

def autho(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/log.html', context)

def logout(request):
    # plot = plots.objects.all()
    context = {
        'title': 'Выход',
        'plots': "ыввфы",
    }
    return render(request, 'users/profile.html', context)