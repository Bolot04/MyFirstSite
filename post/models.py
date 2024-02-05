'''
файл в котором содержится описание базы данных
'''
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    photo = models.ImageField(upload_to="product_photo/%Y/%m/%d", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления\
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

