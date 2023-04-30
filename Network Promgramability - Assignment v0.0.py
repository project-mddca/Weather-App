import requests

# API key for OpenWeatherMap
API_KEY = 'f4a703089e2e872b0a5c010b2c9e3a31'


def get_weather_data(city):

    # API endpoint for fetching weather data
    endpoint = f'http://api.openweathermap.org/data/2.5/weather"{city}&appid={API_KEY}'

    # Make a GET request to the API endpoint
    response = requests.get(endpoint)

    # If the request was successful, return the weather data
    if response.status_code == 200:
        data = response.json()
        return data, print ("This is the current temperature.")
    else:
        print ("Error: Could not retrieve weather data.")