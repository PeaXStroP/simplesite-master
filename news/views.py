from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def news(request):
    news_index = News.objects.all()
    cat = Category.objects.all()
    context = {
        'news': news_index,
        'cat': cat,
        'title': 'Новости',
    }

    return render(request, template_name='news/index.html', context=context)

def show_news(request, post_id):
    current_news = News.objects.get(pk=post_id)
    cat = Category.objects.all()
    context = {
        'current_news': current_news,
        'cat': cat,
    }
    return render(request, template_name='news/show_news.html', context=context)

def categories(request, category_id):
    cat_news = News.objects.filter(category=category_id)
    cat = Category.objects.all()
    current_cat = Category.objects.get(pk=category_id)
    context = {
        'cat_news': cat_news,
        'cat': cat,
        'current_cat': current_cat
    }

    return render(request, template_name='news/categories.html', context=context)
