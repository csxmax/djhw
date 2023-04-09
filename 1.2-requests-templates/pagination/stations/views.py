from csv import DictReader
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as data:
    bus_station_pagi = Paginator(list(map(lambda r: r, DictReader(data))), 10)

def bus_stations(request):
    curr_page_id = int(request.GET.get('page', 1))
    page = bus_station_pagi.get_page(curr_page_id)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
