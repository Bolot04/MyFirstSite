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
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from blog import settings
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


@login_required
def products_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        categories = Category.objects.all()
        selected_category = request.GET.get('category')
        search = request.GET.get('search')
        order = request.GET.get('order')
        if selected_category:
            category = get_object_or_404(Category, title=selected_category)
            products = products.filter(category=category)
        elif search:
            products = products.filter(
                Q(title__icontains=search)
            )
        elif order == 'title':
            products = products.order_by('title')
        elif order == '-title':
            products = products.order_by('-title')
        elif order == 'created_at':
            products = products.order_by('created_at')
        elif order == '-created_at':
            products = products.order_by('-created_at')
        else:
            products = products.exclude(user=request.user)

        max_page = products.__len__() / settings.PAGE_SIZE

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        page = int(request.GET.get('page', 1))

        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE

        products = products[start:end]

        context = {
            "products": products,
            "selected_category": selected_category,
            "categories": categories,
            "pages": range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {  # Нужен для html для получения всех полей продукта
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


def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm(instance=product)
        }
        return render(request, 'products/product_update.html', context)
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(f'/product/{product.id}/')
        return render(request, 'products/product_update.html', {"form": form})


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
