from django.urls import path
from .views import bboard

urlpatterns = [
    path('', bboard, name='bboard')
]
