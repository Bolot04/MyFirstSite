'''
файл для того что-бы работать с админ панелью
'''

from django.contrib import admin
from post.models import Product


admin.site.register(Product)
