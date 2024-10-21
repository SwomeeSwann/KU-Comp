
# Inputs
'''file_input = input("What weather file would you like to open?\n")

# Data and File Init
data = []


# Parsing data to display it
with open(file_input, 'r') as file:
    for line in file:
        line = line.strip()
        data.append(line)


for i in range(0, len(data)):
    data[i] = data[i].split(" ")

    data[i][0] = data[i][0].replace(":", "")

# Data Type Input
data_type = input("What data type would you like to get\n")
data_index = -1

# Find Data Type
for i, row in enumerate(data):
    if data_type in row:
        data_index = i


# Gets dates and their index
first_date = input("From what date (inclusive)\n")
end_date = input("To what date (inclusive)\n")

first_date_index = data[0].index(first_date)
end_date_index = data[0].index(end_date)

display_type = input("What data would you like (Max)(Min)(All)")

# Prints to the user data on given dates
if display_type.lower() == "all":
    for i in range(first_date_index, end_date_index + 1):
        print(data[data_index][i])
elif display_type.lower() == "min":
    for i in range(1, len(data[data_index])):
        minimum = data[data_index][1]
        if float(data[data_index][i]) < float(minimum):
            minimum = data[data_index][i]

    print(minimum)
elif display_type.lower() == "max":
    for i in range(1, len(data[data_index])):
        maximum = 0
        if float(data[data_index][i]) > maximum:
            maximum = data[data_index][i]

    print(maximum)'''





# THIS IS AI 

import requests
import json
import statistics

data = []

def parse_data(file_input, data):
    with open(file_input, 'r') as file:
        for line in file:
            line = line.strip()
            data.append(line)


    for i in range(len(data)):
        data[i] = data[i].split(" ")
        data[i][0] = data[i][0].replace(":", "")


def get_data(first_date, end_date, display_type, data_type, data):

    data_index = 0

    for i, row in enumerate(data):
        if data_type in row:
            data_index = i

    first_date_index = data[0].index(first_date)
    end_date_index = data[0].index(end_date)

    averageList = []
    for dates in range(first_date_index, end_date_index + 1):
        averageList.append(float(data[i][dates]))
    average = statistics.mean(averageList)


    # Prints to the user data on given dates
    if display_type.lower() == "all":
        all_list = []
        for i in range(first_date_index, end_date_index + 1):
            all_list.append(data[data_index][i])
        return all_list
    elif display_type.lower() == "min":
        minimum = min(float(data[data_index][i]))
        print(data_type, minimum)
        return minimum
    elif display_type.lower() == "max":
        maximum = max(float(data[data_index][i]))
        print(data_type, maximum)
        return maximum
    elif display_type.lower() == "average":
        print(data_type, average)
        return average



if __name__ == "__main__":
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

    display_type = input("What data would you like (Max)(Min)(Average)(All)")

    get_data(first_date, end_date, display_type, data_type, data)