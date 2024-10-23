import requests
import tkinter as tk
from PyQt5.QtWidgets import *
import sys

weather_data = {
    "date": "2024-04-30",
    "values": "71.0 50.3423 41.3144 0.2304991 12.320984 50.0",
}

delete_data = {
    "date": "2024-04-29"
}

app = QApplication([])
window = QWidget()


def on_button_clicked():
    data_type = type_text.text()
    date = data_text.text()
    if not data_type == "" and not date == "":

        api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"
        request_response = requests.post(api_url, json=weather_data)
        print(request_response.text)

        #put_response = requests.put(api_url, json=weather_data)

        #date = "2024-04-28"
        #delete_response = requests.delete(api_url, json=date)

        get_response = requests.get(api_url)
        get_output_label.setText(get_response.text.replace("\"", ""))
    else:
        get_output_label.setText("You can't get data with no inputs!")


get_output_label = QLabel("What weather data would you like to see?")
get_output_label.setStyleSheet("font-size: 24px;")

window_layout = QVBoxLayout()

type_text = QLineEdit()
type_text.setPlaceholderText("Enter your data (Ex: weather_code)")
type_text.show()
type_text.setStyleSheet("""
    background-color: black;
    color: white;


""")

data_text = QLineEdit()
data_text.setPlaceholderText("Enter your date (yyyy-mm-dd)")
data_text.show()
data_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }


""")

get_data_date = QPushButton('Click')
get_data_date.clicked.connect(on_button_clicked)
get_data_date.setStyleSheet("""
    QPushButton {
    background-color: lightblue; 
    color: white;
    border: none;
    border-radius: 15px;
    padding: 10px 20px;
    }

    QPushButton:hover {
        background-color: deepskyblue;
    }

    QPushButton:pressed {
        background-color: dodgerblue
    }
                            """)
get_data_date.show()


window_layout.addWidget(data_text)
window_layout.addWidget(type_text)
window_layout.addWidget(get_output_label)
window_layout.addWidget(get_data_date)

window.setLayout(window_layout)


window.setGeometry(100, 100, 400, 150)
window.show()

sys.exit(app.exec())


