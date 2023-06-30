from django.shortcuts import render
from django.http import HttpResponse
from .models import Bboard, Category


def bboard(request):
    bb = Bboard.objects.all()
    cat = Category.objects.all()
    context = {
        'bb': bb,
        'cat': cat,
        'title': 'Объявления',

    }
    return render(request, template_name='bboard/index.html', context=context)


def show_bboard(request, category_id):
    current_bb = Bboard.objects.filter(category=category_id)
    cat = Category.objects.all()
    current_cat = Category.objects.get(pk=category_id)
    context = {
        'current_bb': current_bb,
        'cat': cat,
        'current_cat': current_cat
    }

    return render(request, template_name='bboard/show_bboard.html', context=context)
