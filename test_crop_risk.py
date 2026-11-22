
from ai_weather.weather_api import get_weather
from ai_weather.crop_risk import analyze_crop_risk

# Bengaluru sample coordinates
latitude = 12.9716
longitude = 77.5946

print("Fetching weather data...")

weather = get_weather(latitude, longitude)

print("\nCROP RISK ALERTS")
print("-------------------------")

alerts = analyze_crop_risk(weather)

for alert in alerts:
    print("\nDate:", alert["date"])
    print("Risk:", alert["risk"])
    print("Message:", alert["message"])
