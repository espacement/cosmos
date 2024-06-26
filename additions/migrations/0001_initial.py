# Generated by Django 4.2.13 on 2024-05-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='assets', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
                'db_table': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_news', models.CharField(max_length=150, verbose_name='Название новости')),
                ('image_news', models.ImageField(blank=True, null=True, upload_to='assets', verbose_name='Изображение новости')),
                ('text_news', models.CharField(max_length=500, verbose_name='Текст новости')),
                ('link_news', models.CharField(max_length=500, verbose_name='Ссылка на новость')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
    ]
