import requests
import tkinter as tk


window = tk.Tk()
window.title("Window")
window.geometry("600x600")

def handle_button_press(event):
    data_type = data_box.get()
    date = date_box.get()

    api_url = f"http://localhost:8000/?date={date}&data_type={data_type}"

    response = requests.get(api_url)



button = tk.Button(window, text="Get Data", width=15, height=5)
button.bind("<Button-1>", handle_button_press)
button.place(x=250, y=250)

data_box = tk.Entry(window, width=40)
data_box.place(x=100, y=100)

date_box = tk.Entry(window, width=40)
date_box.place(x=100, y=200)

window.mainloop()

