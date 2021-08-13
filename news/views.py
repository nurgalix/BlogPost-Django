from django.shortcuts import render
from django.http import HttpResponse

from .models import News


# контроллер(вьюшка) отрабатывает клиентский запрос, запрашивает данные у модели и возвращает ответ в виде представление
# заполнненные этими данными
# некий связующие звено между моделями(данные) и представлениями(отображения)


def index(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

