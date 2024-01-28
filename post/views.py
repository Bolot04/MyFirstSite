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
'''

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


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
