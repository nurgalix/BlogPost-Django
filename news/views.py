from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewForm


# контроллер(вьюшка) отрабатывает клиентский запрос, запрашивает данные у модели и возвращает ответ в виде представление
# заполнненные этими данными
# некий связующие звено между моделями(данные) и представлениями(отображения)


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewForm()
    return render(request, 'news/add_news.html', {'form': form})
