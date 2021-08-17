from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


# контроллер(вьюшка) отрабатывает клиентский запрос, запрашивает данные у модели и возвращает ответ в виде представление
# заполнненные этими данными
# некий связующие звено между моделями(данные) и представлениями(отображения)


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})