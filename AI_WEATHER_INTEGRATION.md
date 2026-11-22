# AI + Weather Module - Integration Guide

## 1. Overview

This folder contains the Python AI and Weather modules developed for the Smart Farm Planner project.

The Flask backend can import these functions and use them to process farmer inputs and return results to the frontend.

**Folder:** `ai_weather/`

## 2. Available Functions

| Feature | Python file | Function |
|---|---|---|
| Crop recommendation | crop_recommendation.py | `recommend_crop()` |
| Plant disease detection | disease_detection.py | `detect_disease()` |
| Weather forecast | weather_api.py | `get_weather()` |
| Irrigation planning | irrigation.py | `generate_irrigation_plan()` |
| Crop risk alerts | crop_risk.py | `analyze_crop_risk()` |
| Fertilizer recommendation | fertilizer.py | `recommend_fertilizer()` |
| Harvest prediction | harvest_prediction.py | `predict_harvest()` |
| Market price | agmarknet_price.py | `get_market_prices()` |
| Market comparison | agmarknet_price.py | `compare_markets()` |

## 3. Function Details

### A. Crop Recommendation

```python
from ai_weather.crop_recommendation import recommend_crop

result = recommend_crop(n, p, k, temperature, humidity, ph, rainfall)
```

Inputs: Nitrogen, phosphorus, potassium, temperature, humidity, soil pH and rainfall.

Output: Recommended crop.

### B. Plant Disease Detection

```python
from ai_weather.disease_detection import detect_disease

result = detect_disease(image_path)
```

Input: Uploaded plant leaf image path.

Output: Predicted disease, confidence and top predictions.

### C. Weather Forecast

```python
from ai_weather.weather_api import get_weather

weather = get_weather(latitude, longitude)
```

Inputs: Latitude and longitude.

Output: Seven-day weather forecast and modelled soil moisture information.

### D. Irrigation Planning

```python
from ai_weather.irrigation import generate_irrigation_plan

plan = generate_irrigation_plan(weather)
```

Input: Weather data returned by `get_weather()`.

Output: Irrigation recommendation and reason.

### E. Crop Risk Alerts

```python
from ai_weather.crop_risk import analyze_crop_risk

alerts = analyze_crop_risk(weather)
```

Input: Weather data returned by `get_weather()`.

Output: Weather-related crop risk alerts.

### F. Fertilizer Recommendation

```python
from ai_weather.fertilizer import recommend_fertilizer

result = recommend_fertilizer(n, p, k, ph, crop)
```

Inputs: Soil NPK values, pH and crop name.

Output: General fertilizer options and soil observations.

### G. Harvest Prediction

```python
from ai_weather.harvest_prediction import predict_harvest

result = predict_harvest(crop, sowing_date, maturity_days=None, weather_data=None)
```

Inputs: Crop name, sowing date, optional maturity days and optional weather data.

Output: Estimated harvest date, remaining days, status and weather alerts.

### H. Market Price

```python
from ai_weather.agmarknet_price import get_market_prices, compare_markets

prices = get_market_prices("Karnataka", "Tomato")

comparison = compare_markets(prices)
```

Inputs: State, commodity and optional district.

Output: Market prices, highest modal price and market comparison.

## 4. Integration Flow

1. Frontend sends farmer inputs to Flask backend.
2. Flask backend imports the required Python function.
3. Backend passes the input values to that function.
4. Function processes the data and returns a Python dictionary.
5. Backend converts the result into JSON.
6. Frontend displays the result.

## 5. Important Notes

- Python modules are located inside `ai_weather/`.
- Import functions directly into the Flask backend.
- No separate Flask server is required for these modules.
- Weather information comes from the Open-Meteo API.
- Market prices come from the Agmarknet mandi API.
- Disease detection is preliminary screening, not a confirmed diagnosis.
- Crop, fertilizer, irrigation and harvest recommendations are prototype-level guidance and require local agricultural validation.
- Market prices are reported modal prices,