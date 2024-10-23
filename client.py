import requests
import tkinter as tk
from PyQt5.QtWidgets import *
import sys
import json



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
        date_text.show()
        get_output_button.show()
        get_output_button.setText("Get Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_get_button_clicked)
        get_output_label.show()
    if index == 1:
        mode_combo_box.show()
        data_text.show()
        data_text.setPlaceholderText("Enter your data value (Ex: 60.0 253.0 1.324)")
        date_text.show()
        get_output_button.show()
        get_output_button.setText("Add Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_post_button_clicked)
        get_output_label.show()
    if index == 2:
        mode_combo_box.show()
        type_text.show()
        date_text.show()
        data_text.setPlaceholderText("Enter your data value (Ex: 60.0)")
        data_text.show()
        get_output_button.show()
        get_output_button.setText("Change Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_put_button_clicked)
        get_output_label.show()
    if index == 3:
        mode_combo_box.show()
        date_text.show()
        get_output_button.show()
        get_output_button.setText("Delete Data")
        get_output_button.clicked.disconnect()
        get_output_button.clicked.connect(on_delete_button_clicked)
        get_output_label.show()

def on_mode_index_change():
    selected_index = mode_combo_box.currentIndex()
    hide_all(main_layout)
    new_mode_show(selected_index)


def on_get_button_clicked():
    data_type = type_text.text()
    date = date_text.text()
    if not data_type == "" and not date == "":

        api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"


        

        get_response = requests.get(api_url)
        get_output_label.setText(get_response.text.replace("\"", ""))
    else:
        get_output_label.setText("You can't get data with no inputs!")

def on_post_button_clicked():
    data_values = data_text.text()
    date = date_text.text()
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
    date = date_text.text()
    data_value = data_text.text()
    if not data_type == "" and not date == "":

        api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"

        weather_data = {
            "data_type": data_type,
            "value": data_value,
            "date": date
        }

        put_response = requests.put(api_url, json=weather_data)


        get_response = requests.get(api_url)
        get_output_label.setText(get_response.text.replace("\"", ""))
    else:
        get_output_label.setText("You can't get data with no inputs!")

def on_delete_button_clicked():
    date = date_text.text()
    if not date == "":

        api_url = f"http://localhost:8000/?date={date}"



        delete_response = requests.delete(api_url, json=date)


    else:
        get_output_label.setText("You can't get data with no inputs!")

get_output_label = QLabel("What weather data would you like to see?")
get_output_label.setStyleSheet("font-size: 24px;")




type_text = QLineEdit()
type_text.setPlaceholderText("Enter your data (Ex: weather_code)")
type_text.show()
type_text.setStyleSheet("""
    background-color: black;
    color: white;


""")

date_text = QLineEdit()
date_text.setPlaceholderText("Enter your date (yyyy-mm-dd)")
date_text.show()
date_text.setStyleSheet("""
    QLineEdit {
    background-color: black;
    color: white;
    }

                        

""")

data_text = QLineEdit()
data_text.setPlaceholderText("Enter your data value (Ex: 60.0 253.0 0.324)")
data_text.show()
data_text.setStyleSheet("""
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
mode_combo_box.addItems(["Get Data", "Enter Data", "Change Data", "Delete Data"])
mode_combo_box.currentIndexChanged.connect(on_mode_index_change)


main_layout.addWidget(mode_combo_box)
main_layout.addWidget(date_text)
main_layout.addWidget(data_text)
main_layout.addWidget(type_text)
main_layout.addWidget(get_output_label)
main_layout.addWidget(get_output_button)

data_text.hide()

window.setLayout(main_layout)


window.setGeometry(100, 100, 400, 150)
window.show()

sys.exit(app.exec())


