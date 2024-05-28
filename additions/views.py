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
# 


#                 "title_news": "Новость 1",
#                 "image_news": "assets/photo1.jpg",
#                 "text_news": "Текст новости 1",
#                 "link_news": "public.html",
#             },
#             {
#                 "title_news": "Новость 2",
#                 "image_news": "assets/photo2.jpg",
#                 "text_news": "Текст новости 2",
#                 "link_news": "public.html",
#             },
#             {
#                 "title_news": "Эксперт космической отрасли: совершенно нормально уже говорить о Марсе",
#                 "image_news": "assets/object1.svg",
#                 "text_news": "Российские и китайские ученые обсуждают возможность совместного изучения Марса, заявил научный руководитель Института космических исследований РАН Лев Зеленый",
#                 "link_news": "https://radiosputnik.ru/20240408/mars-1938692234.html",
#             },
#             {
#                 "title_news": "Новость 2",
#                 "image_news": "assets/photo2.jpg",
#                 "text_news": "Текст новости 2",
#                 "link_news": "public.html",
#             },
#             {
#                 "title_news": "Новость 2",
#                 "image_news": "assets/photo2.jpg",
#                 "text_news": "Текст новости 2",
#                 "link_news": "public.html",
#             },
#             {
#                 "title_news": "Эксперт космической отрасли: совершенно нормально уже говорить о Марсе",
#                 "image_news": "assets/object1.svg",
#                 "text_news": "Российские и китайские ученые обсуждают возможность совместного изучения Марса, заявил научный руководитель Института космических исследований РАН Лев Зеленый",
#                 "link_news": "https://radiosputnik.ru/20240408/mars-1938692234.html",
#             },