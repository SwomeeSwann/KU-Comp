import datetime
import time
from open_weather_API import *

def date_to_unix(date):

    # assigned regular string date
    date_list = []
    date_list = date.split('-')
    
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]

    date_time = datetime.datetime(year, month, day, 0, 0, 0)
    return (time.mktime(date_time.timetuple()))

def highest_temperature(unix_date, lat, lon):
    temperature = set()
    
    #start measuring temp at 14:00; ends at 16:00
    start_time = unix_date + 50400
    end_time = unix_date + 57600

    for second in range(start_time, end_time, 300):
        day_data = get_api_data(lat, lon, second)
        total_data[unix_date] = day_data
        temperature = day_data['data'][0]['temp']
    return temperature

#Save data to prevent future calculations
total_data = {}