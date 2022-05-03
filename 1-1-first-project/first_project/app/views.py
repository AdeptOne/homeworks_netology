from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time.strftime("%H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    list_of_current_directories = os.listdir('./')

    for index, directory in enumerate(list_of_current_directories):
        list_of_current_directories[index] = f'<p>{index + 1}: {directory}</p>'

    return HttpResponse(list_of_current_directories)


