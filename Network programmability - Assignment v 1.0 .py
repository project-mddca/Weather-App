import requests


# Set up the API endpoint URL and parameters
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London,UK",
    "appid": "f4a703089e2e872b0a5c010b2c9e3a31",
    "units": "metric"
}
# Send a request to the API
response = requests.get(url, params=params)

# If the response was successful, parse the JSON data and print the current temperature
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"The current temperature in {params['q']} is {temperature}°C.")
else:
    print("Error: could not retrieve weather data.")
