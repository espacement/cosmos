from django.db import models

class plots(models.Model):
    price = models.DecimalField( default=0, max_digits=7, decimal_places=2, verbose_name="Цена")
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='assets', blank=True, null = True, verbose_name="Изображение")
    
    class Meta:
        db_table = "plot"
        verbose_name = "Участок"
        verbose_name_plural = "Участки"