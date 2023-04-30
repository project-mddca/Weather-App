# weather app Final Version with working GUI

import tkinter as tk
import requests

# API key for OpenWeatherMap
API_KEY = 'f4a703089e2e872b0a5c010b2c9e3a31'


# API endpoint for fetching weather data - contacts the API and bring back data
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# function - this outputs the user the weather and brings back, temperature and feels like weather information
def show_weather():
    city = city_entry.get()
    data = get_weather(city)
    if data['cod'] == 200:
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_label.config(text=f'{city}: {description}, {temp:.1f}°C (Feels like: {feels_like:.1f}°C)')

# If the request was successful, return the weather data
    else:
        weather_label.config(text='Error: City not found')

# GUI starts
root = tk.Tk()
root.title('Weather App')

# request input of City as per feedback

# user input 1
city_label = tk.Label(root, text='Enter a city:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

# user input 2 (click 'Get Weather')
button = tk.Button(root, text='Get Weather', command=show_weather)
button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()
