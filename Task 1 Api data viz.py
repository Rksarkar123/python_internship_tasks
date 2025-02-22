import requests
import matplotlib.pyplot as plt
import seaborn as sns
import json


API_KEY = "your_api_key"  # Replace with your actual API key
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    
   
    weather_params = {
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Pressure (hPa)": data["main"]["pressure"],
    }
    
  
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(weather_params.keys()), y=list(weather_params.values()), palette="coolwarm")
    plt.title(f"Weather Data for {CITY}")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.show()
    
else:
    print("Failed to retrieve data. Check your API key and city name.")