
from ai_weather.crop_recommendation import recommend_crop

result = recommend_crop(
    90,     # Nitrogen
    42,     # Phosphorus
    43,     # Potassium
    25,     # Temperature
    80,     # Humidity
    6.5,    # pH
    200     # Rainfall
)

print(result)
