from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import datetime

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Pabna'
      
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid=63b8d7c983e69c3bf000873280336200'
    PARAMS = {'units': 'metric'}
    
    API_KEY = 'AIzaSyAE0DpcozWlK_7ZK2-HMKWlktBU_1Eg9Es'
    SEARCH_ENGINE_ID = '851edd1f8f57e4c45'
    query = city
    page = 1
    start = (page-1) 
    searchType = 'image'
    city_url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imageSize=xlarge'
    
    data = requests.get(city_url).json()
    count = 1
    search_items = data["items"]
    image_url = search_items[1]['link']    
    
    try:
        data = requests.get(url = URL, params = PARAMS)
        res = data.json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temp = res['main']['temp']
        day = datetime.date.today()
        return render(request,'weather/home.html', 
        {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city, 'exception':False, 'image_url':image_url })
        
    except:
        exception=True        
        messages.error(request, 'Your City Is Not Available')
        day = datetime.date.today()
        return render(request,'weather/home.html', 
        {'description':'clear sky', 'icon':'01d', 'temp':25, 'day':day, 'city':'Dhaka', 'exception':True})
        
    

    
