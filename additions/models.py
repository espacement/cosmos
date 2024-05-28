from django.db import models

class news(models.Model):
    title_news = models.CharField(max_length=150, verbose_name="Название новости")
    image_news = models.ImageField(upload_to='assets', blank=True, null = True, verbose_name="Изображение новости")
    text_news = models.CharField(max_length=500, verbose_name="Текст новости")
    link_news = models.CharField(max_length=500, verbose_name="Ссылка на новость")

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class gallery(models.Model):
    image = models.ImageField(upload_to='assets', blank=True, null = True, verbose_name="Изображение")
    
    class Meta:
        db_table = "gallery"
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
      