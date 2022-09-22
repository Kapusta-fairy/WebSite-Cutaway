from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    url = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
