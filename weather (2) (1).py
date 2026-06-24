import requests

city = input("Enter city name: ")

api_key = "670b770fd3db55db248aa22a81319bf8"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Visibility:", data["visibility"], "meters")
    print("Country:", data["sys"]["country"])
else:
    print("City not found. Please check the city name and try again.")
