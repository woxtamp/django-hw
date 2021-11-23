import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_raw = os.listdir()
    files = ''
    for item in files_raw:
        item = item + ', '
        files += item
    msg = f'Список файлов в рабочей директории: {files[:-2]}'
    return HttpResponse(msg)
