from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


API_KEY = '2d3853592cee4f5c8e6214149250107'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City parameter is required'},
                         status=status.HTTP_400_BAD_REQUEST)
    
    params = {
        'q': city,
        'key': API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params = params)
        data = response.json()

        if response.status_code != 200 or 'error' in data:
            return Response({'error': data.get('error', 'Unable to fetch weather')}, 
                            status=response.status_code)

        weather_info = {
            'city': data['location']['name'],
            'temp': data['current']['temp_c'],
            'wind': data['current']['wind_kph'],
        }

        return Response(data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# For Testing: curl "http://api.weatherapi.com/v1/current.json?key=2d3853592cee4f5c8e6214149250107&q=c_name"
