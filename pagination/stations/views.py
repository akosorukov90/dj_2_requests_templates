from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stops = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stops.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stops, settings.POST_ON_PAGE)
    page = paginator.get_page(page_number)
    page_objects = page.object_list
    return render(request, 'stations/index.html', context={
        'bus_stations': page_objects,
        'page': page_number,
    })
