import requests


# Set up the API endpoint URL and parameters
url = "http://api.openweathermap.org/data/2.5/weather?"
params = {
    "lat": "44.36",
    "lon": "39.64,"
    "appid": "f4a703089e2e872b0a5c010b2c9e3a31",
    "units": "metric"
}
# Send a request to the API
response = requests.get (f'http://api.openweathermap.org/data/2.5/weather?"{q}&appid={appid}')

# If the response was successful, parse the JSON data and print the current temperature
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"The current temperature in {params['q']} is {temperature}°C.")
else:
    print("Error: could not retrieve weather data.")
