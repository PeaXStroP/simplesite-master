from django.shortcuts import render
from django.http import HttpResponse


def bboard(request):
    return HttpResponse('Тут будут объявления')
