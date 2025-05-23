import requests

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    API_KEY = "11ab588bbc93ac63170fa0cb7f4d4251"
    city = input("Enter city name: ")
    try:
        weather_data = fetch_weather(city, API_KEY)
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
    except requests.HTTPError as e:
        print("Failed to fetch weather data:", e)