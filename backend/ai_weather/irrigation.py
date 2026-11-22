
def generate_irrigation_plan(
    weather_data,
    area_acres=1.0,
    moisture_threshold=0.25
):

    hourly = weather_data["hourly"]
    daily = weather_data["daily"]

    soil_moisture = hourly[
        "soil_moisture_7_to_28cm"
    ][0]

    rainfall = daily["precipitation_sum"][0]

    rain_probability = daily[
        "precipitation_probability_max"
    ][0]

    evapotranspiration = daily[
        "et0_fao_evapotranspiration"
    ][0]

    # Default water requirement
    water_required_litres = 0.0

    if soil_moisture < moisture_threshold:

        if rainfall >= 2 and rain_probability >= 60:

            recommendation = "Wait for expected rainfall"
            reason = "Soil moisture is low, but rain is forecast."

        else:

            recommendation = "Irrigation may be required"
            reason = "Soil moisture is below the prototype threshold."

            # Estimate water required
            target_moisture = 0.30
            root_zone_depth = 0.21
            application_efficiency = 0.85

            moisture_deficit = max(
                0,
                target_moisture - soil_moisture
            )

            area_square_metres = area_acres * 4046.86

            water_required_litres = (
                area_square_metres
                * root_zone_depth
                * moisture_deficit
                * 1000
                / application_efficiency
            )

            water_required_litres = round(
                water_required_litres, 2
            )

    else:

        recommendation = "No immediate irrigation"
        reason = "Modelled root-zone moisture is above the prototype threshold."

    return {
        "soil_moisture": soil_moisture,
        "forecast_rainfall_mm": rainfall,
        "rain_probability_percent": rain_probability,
        "evapotranspiration_mm": evapotranspiration,
        "water_required_litres": water_required_litres,
        "area_acres": area_acres,
        "recommendation": recommendation,
        "reason": reason
    }
