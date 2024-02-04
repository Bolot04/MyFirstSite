'''
файл для того что-бы работать с админ панелью
'''

from django.contrib import admin
from post.models import Product, Category, Comment


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)

