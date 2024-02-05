'''
файл в котором мы будем помещать "представления" нашего приложения

FBV (function-based views)-представления,  основанные на функциях
CBV (class-based views)-представления, основанные на классах

http - протокол передачи гипер текста
request - объект который содержит информацию о запросе

Method - метод который был использован для отправки запроса
GET - получение данных
POST - отправка данных
PUT - обновление данных
DELETE - удаление данных

response - объект который содержит информацию о том что будет возвращено пользователью
status - код состоаяние который будет возвращен пользователью

render - функция которая отображает шаблон и возвращает ответ

QuerySet - набор объектов, полученных в результате запроса к базе данных.

'''

from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from post.forms import ProductCreateForm, CategoryCreateForm, CommentCreateForm
from post.models import Product, Category, Comment


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello its my project!")


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")


def current_view(request):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    return HttpResponse(current_date)


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(
            request,
            'products/products.html',
            context={'products': products, 'name': 'Vasya'}
        )


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            "categories": categories,
        }
        return render(request, 'products/categories.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm()
        }
        return render(request, 'products/products.create.html', context=context)
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/product/')
        context = {  # Если формачка не валидна он вернет обратно
            "form": ProductCreateForm()
        }
        return render(request, 'products/products.create.html', context=context)


def category_create_view(request):
    if request.method == 'GET':
        context = {
            "form": CategoryCreateForm()
        }
        return render(request, 'products/categories.create.html', context=context)
    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/category/')
        context = {  # Если формачка не валидна он вернет обратно
            "form": CategoryCreateForm()
        }
        return render(request, 'products/categories.create.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = { # Нужен для html для получения всех полей продукта
            "product": product,
            'form': CommentCreateForm()
        }
        return render(request, 'products/products_detail.html', context)
    elif request.method == 'POST':
        form = CommentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Comment.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/product/{product_id}/')
        context = {
            'form': form,
        }
        return render(request, 'products/products_detail.html', context)
