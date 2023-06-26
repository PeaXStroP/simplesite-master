from django.db import models


class Bboard(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    content = models.TextField(max_length=300, blank=False, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/bboard/%Y/%m/%d/', blank=False, verbose_name='Фото')
    price = models.FloatField(null=True, blank=False, verbose_name='Цена')
    author = models.CharField(max_length=20, blank=False, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, editable=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
