import requests
import tkinter as tk

weather_data = {
    "data_type": "weather_code",
    "value": "71.0",
    "date": "2024-04-29"
}

delete_data = {
    "date": "2024-04-30"
}

window = tk.Tk()
window.title("Window")
window.geometry("600x600")

def hide_get_ui():
    button.place_forget()
    data_box.place_forget()
    date_box.place_forget()

def show_get_ui():
    button.place(x=250, y=250)
    data_box.place(x=100, y=100)
    date_box.place(x=100, y=200)

def handle_button_press(event):
    data_type = data_box.get()
    date = date_box.get()

    api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"
    #request_response = requests.post(api_url, json=weather_data)
    #print(request_response.text)

    #put_response = requests.put(api_url, json=weather_data)

    date = "2024-04-28"
    delete_response = requests.delete(api_url, json=date)

    get_response = requests.get(api_url)
    print(get_response.text)

def post_mode_handle(event):
    hide_get_ui()
    print("Post Time!")

button = tk.Button(window, text="Get Data", width=15, height=5)
button.bind("<Button-1>", handle_button_press)
button.place(x=250, y=250)

data_box = tk.Entry(window, width=40)
data_box.place(x=100, y=100)

date_box = tk.Entry(window, width=40)
date_box.place(x=100, y=200)

post_mode_button = tk.Button(window, text="Post", width=5, height=5)
post_mode_button.bind("<Button-1>", post_mode_handle)
post_mode_button.place(x=0, y=0)

put_mode_button = tk.Button(window, text="Put", width=5, height=5)
put_mode_button.bind("<Button-1>", post_mode_handle)
put_mode_button.place(x=66, y=0)


window.mainloop()

