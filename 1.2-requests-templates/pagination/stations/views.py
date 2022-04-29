import csv

from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


# По возможности вынести в сервис
def csv_to_dict(path):
    try:
        results = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)
            return results if reader is not None else None
    except FileNotFoundError as e:
        return e


DATA_SET = csv_to_dict(settings.BUS_STATION_CSV)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    if type(DATA_SET) not in (FileNotFoundError, None):
        current_page = int(request.GET.get('page', 1))
        paginator = Paginator(DATA_SET, 10)
        page = paginator.get_page(current_page)

        context = {
            'bus_stations': paginator.get_page(current_page),
            'page': page,
        }
        return render(request, 'stations/index.html', context)
    return HttpResponseNotFound('<h1>Page not found</h1>')


