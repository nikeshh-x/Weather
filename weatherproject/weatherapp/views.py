from django.shortcuts import render
import datetime
import requests

# Create your views here.
def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kathmandu'  # default city

    # API URL with key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=17d707c1cb4816697a86c257604c0f36'
    params = {'units': 'metric'}
    
   

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Safely access nested data
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']  # 🔥 FIX: temp is inside 'main', not directly in root!

        day = datetime.date.today()

        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
        }
    except Exception as e:
        context = {
            'description': 'Error fetching weather data',
            'icon': '01d',
            'temp': 'N/A',
            'day': datetime.date.today(),
            'city': city,
            'error': str(e)
        }

    return render(request, 'index.html', context)
