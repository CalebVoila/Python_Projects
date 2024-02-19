import requests
from tkinter import Tk, Label, Entry, Button

def get_weather():
    city = city_entry.get()
    api_key = "3be004221c3b2eb0eee1ee5c5da1b6df"  # Replace with user API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'weather' in data and 'main' in data:
        weather_info = f"Weather: {data['weather'][0]['description']}\nTemperature: {data['main']['temp']}°C\nHumidity: {data['main']['humidity']}%"
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="Error: Weather data not available for this location.")

root = Tk()
root.title("Weather Dashboard")

city_label = Label(root, text="Enter city:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = Label(root, text="")
weather_label.pack()

root.mainloop()
