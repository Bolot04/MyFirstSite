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

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from post.models import Product, Category


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


def products_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except:
            return render(
                request,
                'errors/404.html',
            )

        return render(
            request,
            'products/products_detail.html',
            context={'product': product}
        )


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            "categories": categories,
        }
        return render(request, 'products/categories.html', context=context)
