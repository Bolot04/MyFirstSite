'''
файл в котором содержится описание базы данных
'''
from django.db import models


class Product(models.Model):
    photo = models.ImageField(upload_to="product_photo/%Y/%m/%d", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    updated_at = models.DateTimeField(auto_now=True) # Дата последнего обновления

    def __str__(self):

        return f'{self.id} - {self.title}'
