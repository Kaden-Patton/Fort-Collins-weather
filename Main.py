import requests
from bs4 import BeautifulSoup
import json
from Station import Station
import tkinter as tk
from tkinter import PhotoImage, ttk
from tkcalendar import DateEntry
import sys

def submit():
    name = dropdown_var.get()
    id = get_stations()[name]
    start_date = start_calendar.get_date()
    end_date = end_calendar.get_date()
    show_plot(name, id, start_date, end_date)

def get_stations():
    url = "https://climate.colostate.edu/data_access_new.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    dropdown = soup.find("select", {"name": "menu1"})

    stations = {}
    for option in dropdown.find_all("option"):
        station_id = option["value"]
        station_name = option.text.strip()
        stations[station_name] = station_id
    return stations

def show_plot(name, id, start, end):
    url = "https://data.rcc-acis.org/StnData?sid={}&sdate={}&edate={}&elems=1,2,4,10"
    response = requests.get(url.format(id, start, end))
    data = json.loads(response.text)
    station = Station({"name": name, "ID": id})

    for entry in data["data"]:
        station.add_data(entry[0], entry[1], entry[2], entry[3], entry[4])

    station.clean_data()
    station.plot_data_plotly()

def show_about():
    about_window = tk.Toplevel(window)
    about_window.title("About")
    about_window.geometry("400x100")
    about_window.configure(bg="#212121")
    about_window.iconbitmap(f"{sys.path[0]}/icon.ico")

    about_label = ttk.Label(about_window, text="All data sourced from the Colorado Climate Center at CSU", style="TLabel")
    about_label.pack(pady=20)

    about_label2 = ttk.Label(about_window, text="https://climate.colostate.edu/data_access_new.html", style="TLabel")
    about_label2.pack(pady=5)

window = tk.Tk()
window.title("Colorado Historic Weather Data")
window.geometry("400x300")
window.configure(bg="#212121")
window.iconbitmap(f"{sys.path[0]}/icon.ico")

label_style = ttk.Style()
label_style.configure("TLabel", background="#212121", foreground="#FFFFFF")

dropdown_style = ttk.Style()
dropdown_style.configure("TCombobox", fieldbackground="#FFFFFF", background="#424242", foreground="#000000")

button_style = ttk.Style()
button_style.configure("RoundedButton.TButton", borderwidth=0, relief="flat", background="#212121", foreground="#000000", padding=10)
button_style.map("RoundedButton.TButton",
                 background=[("active", "#212121")],
                 foreground=[("active", "#000000")])

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="More", menu=about_menu)

dropdown_label = ttk.Label(window, text="Select station:", style="TLabel")
dropdown_label.pack(pady=10)

options = []
for name in get_stations():
    options.append(name)

dropdown_var = tk.StringVar(window)
dropdown_var.set(options[0])
dropdown = ttk.Combobox(window, textvariable=dropdown_var, values=options, style="TCombobox")
dropdown.pack(pady=5)

start_label = ttk.Label(window, text="Start Date:", style="TLabel")
start_label.pack()

start_calendar = DateEntry(window, width=12, background='#FFFFFF', foreground='#000000', borderwidth=2)
start_calendar.pack(pady=5)

end_label = ttk.Label(window, text="End Date:", style="TLabel")
end_label.pack()

end_calendar = DateEntry(window, width=12, background='#FFFFFF', foreground='#000000', borderwidth=2)
end_calendar.pack(pady=5)

submit_button = ttk.Button(window, text="Submit", command=submit, style="RoundedButton.TButton")
submit_button.pack(pady=10)
window.mainloop()
