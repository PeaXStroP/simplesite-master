from django.urls import path
from .views import news, show_news, categories

urlpatterns = [
    path('', news, name='news'),
    path('post/<int:post_id>/', show_news, name='show_news'),
    path('<int:category_id>/', categories, name='categories')
]
