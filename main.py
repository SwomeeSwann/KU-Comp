import statistics
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
from date_comparison import *
from open_weather_API import *
from datetime import datetime
from math import ceil

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
        data[data_index][i-6] = float(data[data_index][i-6])
        all_list.append(data[data_index][i-6])


    # Prints to the user data on given dates
    if display_type.lower() == "delete":
        all_list = []
        for i in range(end_date_index + 1, first_date_index + 1, -1):
            all_list.append(data[data_index][i-6]) 
        return all_list
    if display_type.lower() == "all":
        print('All data of',data_type, all_list) 
        return all_list
    elif display_type.lower() == "min":
        min_list = []
        for i in range(first_date_index, end_date_index + 1):
            min_list.append(data[data_index][i])
        minimum = float(min(min_list))
        print(data_type, " min: ", minimum)
        return minimum
    elif display_type.lower() == "max":
        max_list = []
        for i in range(first_date_index, end_date_index + 1):
            max_list.append(data[data_index][i])
        maximum = float(max(max_list))
        print(data_type, " max: ", maximum)
        return maximum
    elif display_type.lower() == "average":
        print(data_type, " average: ", average)
        average = statistics.mean(all_list)
        return average
    elif display_type.lower() == "single":
        i = data[0].index(first_date)
        return float(data[data_index][i])
    elif display_type.lower() == "histogram":
            all_list = []
            date_list = []
            for i in range(first_date_index, end_date_index + 1):
                all_list.append(data[0][i])
                date_list.append(float(data[data_index][i]))
            print('All data of',data_type, all_list) 

            fig = plt.figure(figsize=(10, 5))

            plt.bar(all_list, date_list, color = 'blue', width = 0.4)
            plt.xlabel('Dates')
            plt.ylabel(data_type)
            plt.show()

def date_to_index(date):
    date_index = data[0].index(date)
    everything = []
    for i in range(len(data)):
        everything.append(data[data_index][i])
    return everything



#####################################################################################################################################
if __name__ == "__main__":
    liveData = input('Do you want to access live data?\n')
    #API
    if liveData.lower() == 'yes':
        lat = input("Enter the city's latitude: ")
        lon = input("Enter the city's longitude: ")
        time = input('What time would you like to check: ')
        weather_data = get_api_data(lat, lon, time)


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

        print(get_data(first_date, end_date, display_type, data_type, data))