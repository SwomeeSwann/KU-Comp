import http.server
import tkinter
from urllib.parse import urlparse, parse_qs
import main
import json

FILE = "weatherdata.txt"
line_indexes = ["date", "weather_code", "temperature_max", "temperature_min", "precipitation_sum", "wind_speed_max", "precipitation_probability_max"]

class ServerDataHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)

        weather_begin_date = query_parameters.get('begin_date')[0]
        weather_end_date = query_parameters.get('end_date')[0]
        data_type = query_parameters.get('data_type')[0]
        histogram_checked = query_parameters.get('histogram')[0]
        if weather_end_date.lower() == "none":
            data = []

            with open('weatherdata.txt', 'r') as f:
                file_lines = f.readlines()

            if data_type in line_indexes:
                if weather_begin_date in file_lines[0] and len(weather_begin_date) == 10:
                    main.parse_data("weatherdata.txt", data)

                    result = main.get_data(weather_begin_date, weather_begin_date, "single", data_type, data)

                    weather_summary = (f"The {data_type} on {weather_begin_date} is {result}")
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps(weather_summary).encode("utf-8"))
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps(f"The date {weather_begin_date} was not found in database").encode("utf-8"))
            else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps(f"The data type {data_type} does not exist").encode("utf-8"))      
        else:
            data = []

            with open('weatherdata.txt', 'r') as f:
                file_lines = f.readlines()


            if weather_begin_date in file_lines[0] and len(weather_begin_date) == 10 and weather_end_date in file_lines[0] and len(weather_end_date) == 10:
                main.parse_data("weatherdata.txt", data)

                result = main.get_data(weather_begin_date, weather_end_date, "all", data_type, data)
                for i in range(0, len(result)):
                    result[i] = float(result[i])

                if histogram_checked == "True":
                    main.get_data(weather_begin_date, weather_end_date, "histogram", data_type, data)


                weather_summary = (f"The {data_type} on {weather_begin_date} to {weather_end_date} is {result}")
                self.send_response(200)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(weather_summary).encode("utf-8"))

    def do_POST(self):
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)

        weather_data = json.loads(post_data)


        weather_date = weather_data.get('date', 'No Value')
        weather_values = weather_data.get('values', 'No Value')

        with open('weatherdata.txt', 'r') as f:
            file_lines = f.readlines()

        weather_values = weather_values.strip().split(" ")


        if file_lines[0].find(weather_date) == -1:
            for i in range(0, len(line_indexes)):
                if i == 0:
                    file_lines[i] = file_lines[i].strip()
                    file_lines[i] = file_lines[i] + " " + weather_date +" \n"
                else:
                    file_lines[i] = file_lines[i].strip()
                    file_lines[i] = file_lines[i] + " " + weather_values[i - 1] + " \n"


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
        

        if not file_lines[0].find(weather_date) == -1 and data_type in line_indexes:
            
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
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)

        weather_date = json.loads(post_data)

        with open('weatherdata.txt', 'r') as f:
            file_lines = f.readlines()

        data = []

        main.parse_data("weatherdata.txt", data)

        if not file_lines[0].find(weather_date) == -1:
            for i in range(len(line_indexes) - 1, 0, -1):
                removal_value = main.get_data(weather_date, weather_date, "single", line_indexes[i], data)
                print(removal_value)
                file_lines[i] = file_lines[i].replace(str(removal_value) + " ", "")
                    
            file_lines[0] = file_lines[0].replace(weather_date + " ", "")
            
            with open('weatherdata.txt', 'w') as f:
                f.writelines(file_lines)
                f.close()

        self.send_response(201)
        self.send_header('Content-type', "application/json")
        self.end_headers()


port = 8000
server_address = ('localhost', port)
httpd = http.server.HTTPServer(server_address, ServerDataHandler)
print(f'Serving on port {port}')
httpd.serve_forever()