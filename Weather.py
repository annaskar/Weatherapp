import requests

API_KEY = "3466bec4e57444aec2ffa7bbe772d003"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']

    print(f"\nWeather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C\n")
else:
    print(f"Error: {response.status_code}")
    print("Response text:", response.text)
