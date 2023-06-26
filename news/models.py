from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(max_length=1200, blank=False, verbose_name='Контент')
    author = models.CharField(max_length=20, blank=False, verbose_name='Автор')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    update_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')
    is_published = models.BooleanField(default=True, editable=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-publish_date']

    def get_absolute_url(self):
        return reverse('show_news', kwargs={'post_id': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
