
from ai_weather.weather_api import get_weather
from ai_weather.irrigation import generate_irrigation_plan

latitude = 12.9716
longitude = 77.5946

weather = get_weather(latitude, longitude)

result = generate_irrigation_plan(weather)

print("\nAI IRRIGATION PLAN")
print("-------------------------")

for key, value in result.items():
    print(key, ":", value)
