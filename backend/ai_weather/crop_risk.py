
def analyze_crop_risk(weather_data):

    daily = weather_data["daily"]

    alerts = []

    for i in range(len(daily["time"])):

        date = daily["time"][i]

        max_temp = daily["temperature_2m_max"][i]
        rainfall = daily["precipitation_sum"][i]
        rain_probability = daily[
            "precipitation_probability_max"
        ][i]
        evapotranspiration = daily[
            "et0_fao_evapotranspiration"
        ][i]

        if rainfall >= 20:
            alerts.append({
                "date": date,
                "risk": "Heavy rainfall",
                "message": "Heavy rainfall is forecast. Check field drainage."
            })

        if max_temp >= 35:
            alerts.append({
                "date": date,
                "risk": "High temperature",
                "message": "High temperature is forecast. Monitor crop water needs."
            })

        if rainfall < 1 and evapotranspiration >= 5:
            alerts.append({
                "date": date,
                "risk": "Dry weather",
                "message": "Low rainfall and high evapotranspiration may increase water stress."
            })

    if not alerts:
        alerts.append({
            "date": "Next 7 days",
            "risk": "No major weather risk detected",
            "message": "Continue monitoring weather and crop conditions."
        })

    return alerts
