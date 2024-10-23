import requests

def get_api_data(lat, lon, time):
    api_key = '5a614bbef05a248c1de15504b4d61ac1'
    base_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}&units={'imperial'}"
    response = requests.get(base_url)
    weather_data = response.json()    
    return weather_data

    #example of API output
    # {'lat': 40.7685, 'lon': 73.9822, 'timezone': 'Asia/Bishkek', 'timezone_offset': 21600, 
    #  'data': [{'dt': 1456300800, 'sunrise': 1456278425, 'sunset': 1456318085, 
    #            'temp': 42.78, 'feels_like': 42.78, 'pressure': 1026, 'humidity': 21, 
    #            'dew_point': 8.38, 'clouds': 0, 'wind_speed': 1.61, 'wind_deg': 121, 
    #            'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}]}
    temperature = weather_data['data'][0]['temp']
    humidity = weather_data['data'][0]['humidity']
    wind_speed = weather_data['data'][0]['wind_speed']