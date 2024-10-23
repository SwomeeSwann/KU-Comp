import requests
import json
import statistics
import matplotlib.pyplot as plt
import requests
from date_comparison import *

data = []

def parse_data(file_input, data):
    with open(file_input, 'r') as file:
        for line in file:
            line = line.strip()
            data.append(line)
    
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        data[i][0] = data[i][0].replace(":", "")

    return data

def get_data(first_date, end_date, display_type, data_type, data):

    data_index = 0

    for i, row in enumerate(data):
        if data_type in row:
            data_index = i

    first_date_index = data[0].index(first_date)
    end_date_index = data[0].index(end_date)

    all_list = []
    for i in range(first_date_index, end_date_index + 1):
        all_list.append(data[data_index][i])

    if display_type.lower() == "average":
        average = statistics.mean(all_list)


    # Prints to the user data on given dates
    if display_type.lower() == "all":
        print('All data of',data_type, all_list) 
        if len(all_list) == 1:
            return float(all_list[0])
        else:
            return all_list
    elif display_type.lower() == "min":
        minimum = min(float(data[data_index][i]))
        print(data_type, " min: ", minimum)
        return minimum
    elif display_type.lower() == "max":
        maximum = max(float(data[data_index][i]))
        print(data_type, " max: ", maximum)
        return maximum
    elif display_type.lower() == "average":
        print(data_type, " average: ", average)
        return average
    
    elif display_type.lower() == "histogram":
        plt.hist(all_list, bins=len(all_list))
        plt.xlabel(data_type)
        plt.ylabel('Frequency')
        plt.show()

def get_liveWeather_from_api(api_key, lat, lon, time):
    base_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}&units={'imperial'}"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data




if __name__ == "__main__":
    liveData = input('Do you want to access live data?\n')
    #API
    if liveData.lower() == 'yes':
        api_key = '5a614bbef05a248c1de15504b4d61ac1'
        lat = input("Enter the city's latitude: ")
        lon = input("Enter the city's longitude: ")
        time = input('What time would you like to check: ')
        weather_data = get_liveWeather_from_api(api_key, lat, lon, time)
        
        {'lat': 40.7685, 'lon': 73.9822, 'timezone': 'Asia/Bishkek', 'timezone_offset': 21600, 
         'data': [{'dt': 1456300800, 'sunrise': 1456278425, 'sunset': 1456318085, 
                   'temp': 42.78, 'feels_like': 42.78, 'pressure': 1026, 'humidity': 21, 
                   'dew_point': 8.38, 'clouds': 0, 'wind_speed': 1.61, 'wind_deg': 121, 
                   'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}]}
        temperature = weather_data['data'][0]['temp']
        humidity = weather_data['data'][0]['humidity']
        wind_speed = weather_data['data'][0]['wind_speed']


# importing datetime module

 



    #Non-API
    else:
        # Inputs
        file_input = input("What weather file would you like to open?\n")


        # Data and File Init
        data = []


        # Parsing data to display it
        parse_data(file_input, data)


        # Data Type Input
        data_type = input("What data type would you like to get\n")
        data_index = -1


        # Find Data Type


        # Gets dates and their index
        first_date = input("From what date (inclusive)\n")
        end_date = input("To what date (inclusive)\n")

        display_type = input("What data would you like (Max)(Min)(Average)(All)(Histogram)")

        get_data(first_date, end_date, display_type, data_type, data)