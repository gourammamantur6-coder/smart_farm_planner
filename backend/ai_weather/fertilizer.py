
def recommend_fertilizer(n, p, k, ph, crop):

    crop = crop.lower().strip()

    # Crop-wise organic fertilizer database
    organic_fertilizers = {
        "tomato": [
            "Farmyard manure (FYM)",
            "Vermicompost",
            "Neem cake",
            "Compost"
        ],

        "rice": [
            "Farmyard manure (FYM)",
            "Green manure",
            "Compost",
            "Vermicompost"
        ],

        "wheat": [
            "Farmyard manure (FYM)",
            "Vermicompost",
            "Compost"
        ],

        "maize": [
            "Farmyard manure (FYM)",
            "Vermicompost",
            "Neem cake",
            "Green manure"
        ],

        "potato": [
            "Farmyard manure (FYM)",
            "Vermicompost",
            "Compost",
            "Neem cake"
        ],

        "cotton": [
            "Farmyard manure (FYM)",
            "Neem cake",
            "Vermicompost",
            "Green manure"
        ]
    }

    # Crop-wise inorganic fertilizer options
    inorganic_fertilizers = {
        "tomato": ["Urea", "DAP", "MOP", "NPK fertilizer"],
        "rice": ["Urea", "DAP", "MOP"],
        "wheat": ["Urea", "DAP", "NPK fertilizer"],
        "maize": ["Urea", "DAP", "MOP"],
        "potato": ["Urea", "DAP", "MOP"],
        "cotton": ["Urea", "DAP", "MOP"]
    }

    organic = organic_fertilizers.get(
        crop, ["FYM", "Vermicompost", "Compost"]
    )

    inorganic = inorganic_fertilizers.get(
        crop, ["Urea", "DAP", "MOP", "NPK fertilizer"]
    )

    soil_observations = []

    if n < 50:
        soil_observations.append(
            "Nitrogen is relatively low."
        )

    if p < 30:
        soil_observations.append(
            "Phosphorus is relatively low."
        )

    if k < 30:
        soil_observations.append(
            "Potassium is relatively low."
        )

    if ph < 5.5:
        soil_observations.append(
            "Soil is acidic. Check soil-test-based lime requirements."
        )
    elif ph > 7.5:
        soil_observations.append(
            "Soil is alkaline. Check nutrient availability."
        )

    if not soil_observations:
        soil_observations.append(
            "No major issue detected by these screening rules."
        )

    return {
        "crop": crop.title(),
        "organic_fertilizers": organic,
        "inorganic_fertilizers": inorganic,
        "soil_observations": soil_observations,
        "note": (
            "These are general fertilizer options, not confirmed "
            "application recommendations. Select fertilizers and "
            "quantities using crop-specific soil test guidance."
        )
    }
