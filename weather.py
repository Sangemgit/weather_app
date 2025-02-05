import requests

def fetch_hyderabad_weather(api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Hyderabad"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch weather data.")
        return None

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '0e53c6d646984252a62143258242905'
weather_data = fetch_hyderabad_weather(api_key)



if weather_data:
    # Extract relevant information from the weather data
    location = weather_data['location']['name']
    country = weather_data['location']['country']
    temperature_celsius = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    
    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temperature_celsius}°C")
    print(f"Condition: {condition}")
else:
    print("Weather data not available.")
