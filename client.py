import requests
import tkinter as tk
from PyQt5.QtWidgets import *
import sys
import json
from open_weather_API import get_api_data


delete_data = {
    "date": "2024-04-29"
}

app = QApplication([])
window = QWidget()

main_layout = QVBoxLayout()



def hide_all(layout):
    for i in range(0, layout.count() - 1):
        item = main_layout.itemAt(i)
        widget = item.widget()
        widget.hide()


def new_mode_show(index):
    if index == 0:
        mode_combo_box.show()
        type_text.show()
        begin_date_text.show()
        end_date_text.show()
        get_output_button.show()
        get_output_button.setText("Get Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_get_button_clicked)
        get_output_label.show()
    if index == 1:
        mode_combo_box.show()
        data_text.show()
        data_text.setPlaceholderText("Enter your data value (Ex: 60.0 253.0 1.324)")
        begin_date_text.show()
        get_output_button.show()
        get_output_button.setText("Add Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_post_button_clicked)
        get_output_label.show()
        histogram_check.show()
    if index == 2:
        mode_combo_box.show()
        type_text.show()
        begin_date_text.show()
        data_text.setPlaceholderText("Enter your data value (Ex: 60.0)")
        data_text.show()
        get_output_button.show()
        get_output_button.setText("Change Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_put_button_clicked)
        get_output_label.show()
    if index == 3:
        mode_combo_box.show()
        begin_date_text.show()
        get_output_button.show()
        get_output_button.setText("Delete Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_delete_button_clicked)
        get_output_label.show()
    if index == 4:
        mode_combo_box.show()  
        lat_text.show()
        long_text.show()
        time_text.show()
        get_output_button.show()
        get_output_button.disconnect()
        get_output_button.clicked.connect(api_data)
        get_output_button.setText("Get API Data")
        get_output_label.show()


def on_mode_index_change():
    selected_index = mode_combo_box.currentIndex()
    hide_all(main_layout)
    new_mode_show(selected_index)


def on_get_button_clicked():
    data_type = type_text.text()
    begin_date = begin_date_text.text()
    end_date = end_date_text.text()
    if not data_type == "" and not begin_date == "":
        if end_date == "":
            api_url = f"http://localhost:8000/?begin_date={begin_date}&data_type={data_type}"


            

            get_response = requests.get(api_url)
            get_output_label.setText(get_response.text.replace("\"", ""))
        else:
            if histogram_check.isChecked():
                api_url = f"http://localhost:8000/?begin_date={begin_date}&end_date={end_date}&data_type={data_type}&histogram=True"
            else:
                api_url = f"http://localhost:8000/?begin_date={begin_date}&end_date={end_date}&data_type={data_type}&histogram=False"


            get_response = requests.get(api_url)
            get_output_label.setText(get_response.text.replace("\"", ""))
    else:
        get_output_label.setText("You can't get data with no inputs!")


def on_post_button_clicked():
    data_values = data_text.text()
    date = begin_date_text.text()
    if not data_text == "" and not date == "":

        weather_data = {
            "date": date,
            "values": data_values,
        }

        api_url = f"http://localhost:8000/?date={date}&data_type={data_values}"
        request_response = requests.post(api_url, json=weather_data)
        print(request_response.text)

        get_output_label.setText(f"Added {date}")

    else:
        get_output_label.setText("You can't add data with no inputs!")

def on_put_button_clicked():
    data_type = type_text.text()
    date = begin_date_text.text()
    data_value = data_text.text()
    if not data_type == "" and not date == "":

        api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"

        weather_data = {
            "data_type": data_type,
            "value": data_value,
            "date": date
        }

        put_response = requests.put(api_url, json=weather_data)


    else:
        get_output_label.setText("You can't change data with no inputs!")

def on_delete_button_clicked():
    date = begin_date_text.text()
    if not date == "":

        api_url = f"http://localhost:8000/?date={date}"



        delete_response = requests.delete(api_url, json=date)


    else:
        get_output_label.setText("You can't delete data with no inputs!")

def api_data():
    lat = lat_text.text()
    long = long_text.text()
    time = time_text.text()
    if not lat == "" and not long == "" and not time == "":
        api_weather_data = get_api_data(float(lat), float(long), int(time))
        get_output_label.setText(f"The temperature in {lat}, {long} at {time} is {api_weather_data[0]}, the humidity is {api_weather_data[1]}, the wind speed is {api_weather_data[2]} ")
    else:
        get_output_label.setText("You can't get data with no inputs!")

get_output_label = QLabel("What weather data would you like to see?")
get_output_label.setStyleSheet("font-size: 24px;")




type_text = QLineEdit()
type_text.setPlaceholderText("Enter data (Ex: weather_code)")
type_text.show()
type_text.setStyleSheet("""
    background-color: black;
    color: white;


""")

begin_date_text = QLineEdit()
begin_date_text.setPlaceholderText("Enter beginning date (yyyy-mm-dd)")
begin_date_text.show()
begin_date_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        

""")

end_date_text = QLineEdit()
end_date_text.setPlaceholderText("Enter end date (yyyy-mm-dd) *enter none if blank")
end_date_text.show()
end_date_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        

""")

data_text = QLineEdit()
data_text.setPlaceholderText("Enter data value (Ex: 60.0 253.0 0.324)")
data_text.show()
data_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        """)                        

lat_text = QLineEdit()
lat_text.setPlaceholderText("Enter latitude Ex: (38.9822)")
lat_text.show()
lat_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        """)        

long_text = QLineEdit()
long_text.setPlaceholderText("Enter longitude Ex:(-94.6708)")
long_text.show()
long_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        """)        

time_text = QLineEdit()
time_text.setPlaceholderText("Enter time in Unix format (Ex: 1729689573)")
time_text.show()
time_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        """)        

get_output_button = QPushButton('Click')
get_output_button.clicked.connect(on_get_button_clicked)
get_output_button.setStyleSheet("""
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
get_output_button.show()

mode_combo_box = QComboBox()
mode_combo_box.addItems(["Get Data", "Enter Data", "Change Data", "Delete Data", "Get API Data"])
mode_combo_box.currentIndexChanged.connect(on_mode_index_change)


histogram_check = QCheckBox()
histogram_check.setText("Show Histogram")

main_layout.addWidget(mode_combo_box)
main_layout.addWidget(begin_date_text)
main_layout.addWidget(end_date_text)
main_layout.addWidget(data_text)
main_layout.addWidget(type_text)
main_layout.addWidget(lat_text)
main_layout.addWidget(long_text)
main_layout.addWidget(time_text)
main_layout.addWidget(get_output_label)
main_layout.addWidget(get_output_button)
main_layout.addWidget(histogram_check)

data_text.hide()
lat_text.hide()
long_text.hide()
time_text.hide()

window.setLayout(main_layout)


window.setGeometry(100, 100, 400, 150)
window.show()

sys.exit(app.exec())


