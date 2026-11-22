
from ai_weather.weather_api import get_weather
from ai_weather.harvest_prediction import predict_harvest

# Sample farm location
latitude = 12.9716
longitude = 77.5946

# Sample crop details
crop = "Tomato"
sowing_date = "2026-11-01"

# Get weather forecast
print("Fetching weather forecast...")

weather = get_weather(latitude, longitude)

# Generate harvest prediction
result = predict_harvest(
    crop=crop,
    sowing_date=sowing_date,
    weather_data=weather
)

print("\nHARVEST PREDICTION")
print("-------------------------")

for key, value in result.items():
    print(key, ":", value)
