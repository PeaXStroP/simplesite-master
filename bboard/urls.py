from django.urls import path
from .views import bboard, show_bboard

urlpatterns = [
    path('', bboard, name='bboard'),
    path('bb_post/<int:category_id>/', show_bboard, name='show_bboard')
]
