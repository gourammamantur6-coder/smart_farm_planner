
from datetime import datetime, timedelta


# Approximate maturity periods in days.
# Actual duration depends on crop variety and growing conditions.
CROP_MATURITY = {
    "tomato": 90,
    "rice": 120,
    "wheat": 120,
    "maize": 100,
    "potato": 100,
    "cotton": 160,
    "groundnut": 110,
    "sugarcane": 365,
    "onion": 120,
    "chilli": 150,
    "soybean": 100,
    "ragi": 110,
    "sunflower": 100,
    "pulses": 90
}


def predict_harvest(crop, sowing_date, maturity_days=None,
                    weather_data=None):

    crop = crop.lower().strip()

    if maturity_days is None:
        maturity_days = CROP_MATURITY.get(crop)

    if maturity_days is None:
        raise ValueError(
            "Maturity period not available for this crop. "
            "Please provide maturity_days."
        )

    if maturity_days <= 0:
        raise ValueError("Maturity days must be greater than zero.")

    sowing_date = datetime.strptime(
        sowing_date, "%Y-%m-%d"
    ).date()

    today = datetime.now().date()

    harvest_date = sowing_date + timedelta(days=maturity_days)

    days_remaining = (harvest_date - today).days

    if days_remaining > 30:
        status = "Crop is still in its growing period"
    elif days_remaining > 7:
        status = "Harvest is approaching"
    elif days_remaining >= 0:
        status = "Expected maturity is very near"
    else:
        status = "Estimated maturity date has passed; inspect the crop"

    result = {
        "crop": crop.title(),
        "sowing_date": str(sowing_date),
        "expected_maturity_days": maturity_days,
        "estimated_harvest_date": str(harvest_date),
        "days_until_estimated_harvest": days_remaining,
        "harvest_status": status,
        "weather_forecast_alerts": []
    }

    if weather_data:

        daily = weather_data["daily"]

        for i in range(len(daily["time"])):

            rainfall = daily["precipitation_sum"][i]
            rain_probability = daily[
                "precipitation_probability_max"
            ][i]

            if rainfall is not None and rain_probability is not None:
                if rainfall >= 20 and rain_probability >= 60:

                    result["weather_forecast_alerts"].append({
                        "date": daily["time"][i],
                        "rainfall_mm": rainfall,
                        "rain_probability_percent": rain_probability,
                        "alert": (
                            "Heavy rainfall is forecast. "
                            "Inspect crop maturity and plan carefully "
                            "if the crop is ready for harvesting."
                        )
                    })

    result["weather_note"] = (
        "Weather alerts cover only the available 7-day forecast. "
        "They cannot predict weather on the estimated harvest date "
        "when that date is outside the forecast period."
    )

    result["note"] = (
        "Harvest date is approximate. Check actual crop maturity "
        "and local agricultural guidance before harvesting."
    )

    return result
