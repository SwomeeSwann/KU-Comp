import http.server
import json
from urllib.parse import urlparse, parse_qs
import main

FILE = "weatherdata.txt"

class ServerDataHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)

        date = query_parameters.get('date', ['2024-04-24'])[0]
        data_type = query_parameters.get('data_type', ['temperature_min'])[0]
        data = []


        main.parse_data("weatherdata.txt", data)
        result = main.get_data(date, date, "all", data_type, data)

        string = (f"The {data_type} on {date} is {result}")

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(string).encode("utf-8"))


port = 8000
server_address = ('localhost', port)
httpd = http.server.HTTPServer(server_address, ServerDataHandler)
print(f'Serving on port {port}')
httpd.serve_forever()