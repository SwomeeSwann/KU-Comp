
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

# Inputs
file_input = input("What weather file would you like to open?\n")

# Data and File Init
data = []

# Parsing data to display it
with open(file_input, 'r') as file:
    for line in file:
        line = line.strip()
        data.append(line)

for i in range(len(data)):
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
    minimum = min(float(data[data_index][i]) for i in range(1, len(data[data_index])))
    print(minimum)
elif display_type.lower() == "max":
    maximum = max(float(data[data_index][i]) for i in range(1, len(data[data_index])))
    print(maximum)

# API Request
response_API = requests.get("https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM")

# Check if the request was successful
if response_API.status_code == 200:
    data_api = response_API.text
    # Assuming the data is JSON formatted; if not, you need to process it accordingly
    try:
        parsed_json = json.loads(data_api)
        # Access data from parsed_json as needed; this depends on the structure of the JSON
        # For example:
        print(parsed_json)  # Modify as needed based on the JSON structure
    except json.JSONDecodeError:
        print("Response is not in valid JSON format.")
else:
    print(f"Failed to retrieve data: {response_API.status_code}")

#import requests
#import json
#response_API = requests.get(https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM)
#print(response_API.status_code)
#data = response_API.text
#json.loads(data)
#parse_json['']['']['']['active']
