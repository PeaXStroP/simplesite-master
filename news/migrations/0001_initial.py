# Generated by Django 4.1.7 on 2023-06-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(max_length=300, verbose_name='Контент')),
                ('author', models.CharField(max_length=20, verbose_name='Автор')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('publish_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-publish_date'],
            },
        ),
    ]