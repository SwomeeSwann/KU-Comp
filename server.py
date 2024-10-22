import http.server
import json
from urllib.parse import urlparse, parse_qs
import main

FILE = "weatherdata.txt"

class ServerDataHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)

        weather_date = query_parameters.get('date')[0]
        data_type = query_parameters.get('data_type')[0]
        data = []


        main.parse_data("weatherdata.txt", data)

        result = main.get_data(weather_date, weather_date, "all", data_type, data)

        weather_summary = (f"The {data_type} on {weather_date} is {result}")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(weather_summary).encode("utf-8"))

    def do_POST(self):
        line_indexes = ["date", "weather_code", "temperature_max", "temperature_min", "precipitation_sum", "wind_speed_max", "precipitation_probability_max"]
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)

        weather_data = json.loads(post_data)

        data_type = weather_data.get('data_type', 'No Value')
        weather_value = weather_data.get('value', 'No Value')
        weather_date = weather_data.get('date', 'No Value')

        with open('weatherdata.txt', 'r') as f:
            file_lines = f.readlines()

        line_number = line_indexes.index(data_type)
        

        if file_lines[0].find(weather_date) == -1:
            file_lines[line_number] = file_lines[line_number].strip() + " " + weather_value + "\n"
            file_lines[0] = file_lines[0].strip() + " " + weather_date + "\n"

            with open('weatherdata.txt', 'w') as f:
                f.writelines(file_lines)
                f.close()

            self.send_response(201)
            self.send_header('Content-type', "application/json")
            self.end_headers()
        else:
            self.send_response(201)
            self.send_header('Content-type', "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(f"Data for {weather_date} already exists. Try changing it instead").encode("utf-8"))

    def do_PUT(self):
        line_indexes = ["date", "weather_code", "temperature_max", "temperature_min", "precipitation_sum", "wind_speed_max", "precipitation_probability_max"]
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)

        weather_data = json.loads(post_data)

        data_type = weather_data.get('data_type', 'No Value')
        weather_value = weather_data.get('value', 'No Value')
        weather_date = weather_data.get('date', 'No Value')

        with open('weatherdata.txt', 'r') as f:
            file_lines = f.readlines()

        line_number = line_indexes.index(data_type)
        

        if not file_lines[0].find(weather_date) == -1:
            
            weather_date_list = file_lines[0].strip().split(" ")

            weather_value_list = file_lines[line_number].strip().split(" ")

            weather_index = weather_date_list.index(weather_date)

            weather_value_list[weather_index] = weather_value

            new_weather_value = " ".join(weather_value_list)

            file_lines[line_number] = new_weather_value

            file_lines[line_number] = file_lines[line_number] + "\n"
            
            with open('weatherdata.txt', 'w') as f:
                f.writelines(file_lines)
                f.close()

            self.send_response(201)
            self.send_header('Content-type', "application/json")
            self.end_headers()

    def do_DELETE(self):
        line_indexes = ["date", "weather_code", "temperature_max", "temperature_min", "precipitation_sum", "wind_speed_max", "precipitation_probability_max"]
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)

        weather_date = json.loads(post_data)

    
        
        with open('weatherdata.txt', 'r') as f:
            file_lines = f.readlines()

        data = []


        main.parse_data("weatherdata.txt", data)

        date_index = file_lines[0].strip().split(" ").index(weather_date)

        for i in range(0, len(file_lines)):
            weather_value = main.get_data(weather_date, weather_date, "all", line_indexes[i], data) + " "
            file_lines[i] = file_lines[i].strip().split(" ")
            file_lines[i].pop(date_index)
            file_lines[i] = " ".join(file_lines[i]) + "\n"
        

        with open('weatherdata.txt', 'w') as f:
            f.writelines(file_lines)

        self.send_response(201)
        self.send_header('Content-type', "application/json")
        self.end_headers()


port = 8000
server_address = ('localhost', port)
httpd = http.server.HTTPServer(server_address, ServerDataHandler)
print(f'Serving on port {port}')
httpd.serve_forever()