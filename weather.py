import json
import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"

api_key = "8cfe265be4da24d764e7e283ac366c11"
city = input("City(Default is Kathmandu): ")
units = "metric"

if city == "":
    city = "Kathmandu"

params = {
    "q": city, #q is for city because the full url has it as q={cityname}
    "appid": api_key,
    "units": units
}

response = requests.get(base_url, params=params) #params build the full url for us
data = response.json()

if data['cod'] == '404':
    print("City not found.")
else:
    print("----------------------------------------")
    print(f"City: {data['name']}")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print("----------------------------------------")