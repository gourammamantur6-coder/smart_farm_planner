
from ai_weather.weather_api import get_weather

# Sample coordinates: Bengaluru, Karnataka
latitude = 12.9716
longitude = 77.5946

print("Fetching 7-day weather forecast...")

weather = get_weather(latitude, longitude)

daily = weather["daily"]

for i in range(len(daily["time"])):
    print("\nDate:", daily["time"][i])
    print("Maximum temperature:",
          daily["temperature_2m_max"][i], "°C")
    print("Minimum temperature:",
          daily["temperature_2m_min"][i], "°C")
    print("Rainfall:",
          daily["precipitation_sum"][i], "mm")
    print("Rain probability:",
          daily["precipitation_probability_max"][i], "%")
    print("Evapotranspiration:",
          daily["et0_fao_evapotranspiration"][i], "mm")
    
print("\nSOIL MOISTURE INFORMATION")

hourly = weather["hourly"]

print("Date and time:", hourly["time"][0])

print("Surface soil moisture:",
      hourly["soil_moisture_0_to_7cm"][0])

print("Upper root-zone moisture:",
      hourly["soil_moisture_7_to_28cm"][0])

print("Deep soil moisture:",
      hourly["soil_moisture_28_to_100cm"][0])

