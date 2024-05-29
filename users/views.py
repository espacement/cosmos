from django.shortcuts import render

# Create your views here.
def profile(request):
    # plot = plots.objects.all()
    context = {
        'title': 'Профиль',
        'plots': "ыввфы",
    }
    return render(request, 'users/profile.html', context)

def auth(request):
    # plot = plots.objects.all()
    context = {
        'title': 'Авторизация',
        'plots': "ыввфы",
    }
    return render(request, 'users/log.html', context)

def logout(request):
    # plot = plots.objects.all()
    context = {
        'title': 'Выход',
        'plots': "ыввфы",
    }
    return render(request, 'users/profile.html', context)