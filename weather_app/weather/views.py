import requests
from django.shortcuts import render
from .models import City


# Create your views here.

def index(request):
    appID = 'YOUR API KEY, IT CAN BE GENERATED IN YOUR WEATHERMAP SETTINGS'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appID

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'press': res["main"]["pressure"] // 1.333,
            'hum': res["main"]["humidity"],
            'wind': res["wind"]["speed"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'weather/index.html', context)


def about(request):
    return render(request, 'weather/about.html')


def error(request, exception):
    return render(request, 'weather/404.html')
