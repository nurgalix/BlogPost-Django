from django.shortcuts import render
from django.http import HttpResponse


# контроллер(вьюшка) отрабатывает клиентский запрос, запрашивает данные у модели и возвращает ответ в виде представление
# заполнненные этими данными
# некий связующие звено между моделями(данные) и представлениями(отображения)


def index(request):
    print(request)
    return HttpResponse('Hello World')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
