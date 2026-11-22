from flask import Flask, jsonify, request
import database
import requests
from ai_weather.weather_api import get_weather
from ai_weather.crop_risk import analyze_crop_risk
from ai_weather.irrigation import generate_irrigation_plan
from ai_weather.harvest_prediction import predict_harvest
app = Flask(__name__)
@app.route("/api/location-search", methods=["GET"])
def location_search():
    name = request.args.get("name")

    if not name or len(name.strip()) < 2:
        return jsonify({
            "status": "error",
            "message": "Please enter a valid village name"
        }), 400

    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"

        params = {
            "name": name.strip(),
            "count": 5,
            "language": "en",
            "countryCode": "IN"
        }

        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        results = response.json().get("results", [])

        if not results:
            return jsonify({
                "status": "error",
                "message": "Location not found"
            }), 404

        locations = []

        for place in results:
            locations.append({
                "name": place["name"],
                "state": place.get("admin1"),
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "country": place.get("country")
            })

        return jsonify({
            "status": "success",
            "locations": locations
        })

    except requests.RequestException:
        return jsonify({
            "status": "error",
            "message": "Location service is unavailable"
        }), 502

@app.route("/")
def home():
    return jsonify({
        "message": "AI-Powered Smart Agriculture Assistant Backend is running!"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is working"
    })

@app.route("/api/db-test")
def db_test():
    try:
        conn = database.get_connection()
        conn.close()
        return {"status": "success", "message": "MySQL connected!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
    
@app.route("/api/farmers", methods=["POST"])
def register_farmer():
    data = request.get_json()

    name = data.get("name")
    phone = data.get("phone")
    location = data.get("location")

    if not name or not phone or not location:
        return jsonify({
            "status": "error",
            "message": "Name, phone and village are required"
        }), 400

    try:
        conn = database.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO farmers (name, phone, location) VALUES (%s, %s, %s)",
            (name, phone, location)
        )

        conn.commit()
        farmer_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "message": "Farmer registered successfully",
            "farmer_id": farmer_id
        }), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500




@app.route("/api/farmers", methods=["GET"])
def get_farmers():
    try:
        conn = database.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM farmers")
        farmers = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "farmers": farmers
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route("/api/farms", methods=["POST"])
def register_farm():
    data = request.get_json()

    try:
        conn = database.get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO farms
        (farmer_id, farm_name, crop_name, soil_type, area_acres)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            data["farmer_id"],
            data["farm_name"],
            data["crop_name"],
            data["soil_type"],
            data["area_acres"]
        )

        cursor.execute(sql, values)
        conn.commit()

        farm_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "message": "Farm registered successfully",
            "farm_id": farm_id
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route("/api/farms", methods=["GET"])
def get_farms():
    try:
        conn = database.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM farms")
        farms = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "farms": farms
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/api/weather", methods=["GET"])
def weather_forecast():

    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    if not latitude or not longitude:
        return jsonify({
            "status": "error",
            "message": "Latitude and longitude are required"
        }), 400

    try:
        weather_data = get_weather(float(latitude), float(longitude))

        return jsonify({
            "status": "success",
            "weather": weather_data
        })

    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid latitude or longitude"
        }), 400

    except requests.RequestException:
        return jsonify({
            "status": "error",
            "message": "Weather service is unavailable"
        }), 502
@app.route("/api/crop-risk", methods=["GET"])
def crop_risk():

    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    if not latitude or not longitude:
        return jsonify({
            "status": "error",
            "message": "Latitude and longitude are required"
        }), 400

    try:
        weather_data = get_weather(float(latitude), float(longitude))
        alerts = analyze_crop_risk(weather_data)

        return jsonify({
            "status": "success",
            "crop_risk_alerts": alerts
        })

    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid latitude or longitude"
        }), 400

    except requests.RequestException:
        return jsonify({
            "status": "error",
            "message": "Weather service is unavailable"
        }), 502

@app.route("/api/save-weather", methods=["POST"])
def save_weather():

    data = request.get_json() or {}

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if latitude is None or longitude is None:
        return jsonify({
            "status": "error",
            "message": "Latitude and longitude are required"
        }), 400

    conn = None
    cursor = None
    try:
        weather_data = get_weather(float(latitude), float(longitude))
        daily = weather_data["daily"]

        conn = database.get_connection()
        cursor = conn.cursor()


        location = data.get("location", f"{latitude}, {longitude}")

        records = []

        for i in range(len(daily["time"])):
            records.append((
                location,
                daily["temperature_2m_max"][i],
                daily["relative_humidity_2m_mean"][i],
                daily["precipitation_sum"][i],
                daily["time"][i],
                daily["precipitation_probability_max"][i],
                daily["et0_fao_evapotranspiration"][i]
            ))

        for record in records:
            cursor.execute("""
                SELECT id
                FROM weather_records
                WHERE location = %s AND forecast_date = %s
                ORDER BY id DESC
                LIMIT 1
            """, (record[0], record[4]))

            existing = cursor.fetchone()

            if existing:
                cursor.execute("""
                    UPDATE weather_records
                    SET temperature = %s,
                        humidity = %s,
                        rainfall = %s,
                        rain_probability = %s,
                        evapotranspiration = %s
                    WHERE id = %s
                """, (
                    record[1], record[2], record[3],
                    record[5], record[6], existing[0]
                ))
            else:
                cursor.execute("""
                    INSERT INTO weather_records
                    (location, temperature, humidity, rainfall,
                     forecast_date, rain_probability, evapotranspiration)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, record)

        conn.commit()

        return jsonify({
            "status": "success",
            "message": "Weather records saved successfully",
            "records_saved": len(records)
        })

    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid latitude or longitude"
        }), 400

    except requests.RequestException:
        return jsonify({
            "status": "error",
            "message": "Weather service is unavailable"
        }), 502

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/api/save-irrigation", methods=["POST"])
def save_irrigation():

    data = request.get_json() or {}

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    farm_id = data.get("farm_id")

    if latitude is None or longitude is None or farm_id is None:
        return jsonify({
            "status": "error",
            "message": "Latitude, longitude and farm_id are required"
        }), 400

    conn = None
    cursor = None

    try:
        conn = database.get_connection()
        cursor = conn.cursor(dictionary=True)

        # Get actual farm area
        cursor.execute(
            "SELECT area_acres FROM farms WHERE id = %s",
            (farm_id,)
        )

        farm = cursor.fetchone()

        if not farm:
            return jsonify({
                "status": "error",
                "message": "Farm not found"
            }), 404

        area_acres = float(farm["area_acres"])

        # Get weather and calculate irrigation
        weather_data = get_weather(
            float(latitude),
            float(longitude)
        )

        plan = generate_irrigation_plan(
            weather_data,
            area_acres=area_acres
        )

        # Save irrigation plan
        sql = """
        INSERT INTO irrigation_plans
        (
            farm_id,
            soil_moisture,
            forecast_rainfall,
            rain_probability,
            evapotranspiration,
            water_required_litres,
            recommendation,
            reason
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            farm_id,
            plan["soil_moisture"],
            plan["forecast_rainfall_mm"],
            plan["rain_probability_percent"],
            plan["evapotranspiration_mm"],
            plan["water_required_litres"],
            plan["recommendation"],
            plan["reason"]
        )

        cursor.execute(sql, values)
        conn.commit()

        return jsonify({
            "status": "success",
            "message": "Irrigation plan saved successfully",
            "irrigation_plan": plan
        })

    except (ValueError, requests.RequestException) as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/api/weather-records", methods=["GET"])
def get_weather_records():

    try:
        conn = database.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
              SELECT * FROM (
    SELECT w.*
    FROM weather_records w
    INNER JOIN (
        SELECT location, forecast_date, MAX(id) AS latest_id
        FROM weather_records
        GROUP BY location, forecast_date
    ) latest ON w.id = latest.latest_id
    ORDER BY w.forecast_date DESC
    LIMIT 7
) AS next_days
ORDER BY forecast_date ASC
        """)

        records = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "weather_records": records
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@app.route("/api/irrigation-records", methods=["GET"])
def get_irrigation_records():

    conn = None
    cursor = None

    try:
        conn = database.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM irrigation_plans
            ORDER BY id DESC
        """)

        records = cursor.fetchall()

        return jsonify({
            "status": "success",
            "irrigation_records": records
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route("/api/irrigation", methods=["GET"])
def irrigation_recommendation():

    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    farm_id = request.args.get("farm_id")

    if not latitude or not longitude or not farm_id:
        return jsonify({
            "status": "error",
            "message": "Latitude, longitude and farm_id are required"
        }), 400

    connection = None
    cursor = None

    try:
        connection = database.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT area_acres FROM farms WHERE id = %s",
            (farm_id,)
        )

        farm = cursor.fetchone()

        if not farm:
            return jsonify({
                "status": "error",
                "message": "Farm not found"
            }), 404

        area_acres = float(farm["area_acres"])

        weather_data = get_weather(
            float(latitude),
            float(longitude)
        )
        print("Weather data received:", weather_data.keys())

        plan = generate_irrigation_plan(
            weather_data,
            area_acres=area_acres
        )

        return jsonify({
            "status": "success",
            "irrigation_plan": plan
        })

    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid input values"
        }), 400

    except requests.RequestException:
        return jsonify({
            "status": "error",
            "message": "Weather service is unavailable"
        }), 502

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
@app.route("/api/fertilizer-recommendation", methods=["POST"])
def fertilizer_recommendation():

    data = request.get_json() or {}

    required_fields = ["n", "p", "k", "ph", "crop"]

    if any(field not in data for field in required_fields):
        return jsonify({
            "status": "error",
            "message": "N, P, K, pH and crop are required"
        }), 400

    try:
        from ai_weather.fertilizer import recommend_fertilizer

        result = recommend_fertilizer(
            float(data["n"]),
            float(data["p"]),
            float(data["k"]),
            float(data["ph"]),
            str(data["crop"])
        )

        return jsonify({
            "status": "success",
            "fertilizer_recommendation": result
        })

    except (ValueError, TypeError) as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/crop-recommendation", methods=["POST"])
def crop_recommendation():

    data = request.get_json() or {}

    required_fields = [
        "n", "p", "k", "temperature",
        "humidity", "ph", "rainfall"
    ]

    if any(field not in data for field in required_fields):
        return jsonify({
            "status": "error",
            "message": "All crop input values are required"
        }), 400

    try:
        from ai_weather.crop_recommendation import recommend_crop
        result = recommend_crop(
            float(data["n"]),
            float(data["p"]),
            float(data["k"]),
            float(data["temperature"]),
            float(data["humidity"]),
            float(data["ph"]),
            float(data["rainfall"])
        )

        return jsonify({
            "status": "success",
            "crop_recommendation": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
@app.route("/api/disease-detection", methods=["POST"])
def disease_detection():

    from ai_weather.disease_detection import detect_disease

    if "image" not in request.files:
        return jsonify({
            "status": "error",
            "message": "Please upload a plant image"
        }), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({
            "status": "error",
            "message": "No image selected"
        }), 400

    import os
    import tempfile

    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".jpg"
        ) as temp:
            image.save(temp.name)
            image_path = temp.name

        result = detect_disease(image_path)

        return jsonify({
            "status": "success",
            "disease_detection": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if "image_path" in locals() and os.path.exists(image_path):
            os.remove(image_path)
@app.route("/api/market-prices", methods=["GET"])
def market_prices():

    state = request.args.get("state")
    commodity = request.args.get("commodity")
    district = request.args.get("district")

    if not state or not commodity:
        return jsonify({
            "status": "error",
            "message": "State and commodity are required"
        }), 400

    try:
        from ai_weather.agmarknet_price import (
            get_market_prices,
            compare_markets
        )

        result = get_market_prices(state, commodity, district)
        comparison = compare_markets(result)

        return jsonify(comparison)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
@app.route("/api/harvest-prediction", methods=["POST"])
def harvest_prediction():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "JSON data is required"
            }), 400

        crop = data.get("crop")
        sowing_date = data.get("sowing_date")
        maturity_days = data.get("maturity_days")

        if not crop or not sowing_date:
            return jsonify({
                "status": "error",
                "message": "Crop and sowing_date are required"
            }), 400

        result = predict_harvest(
            crop,
            sowing_date,
            maturity_days
        )

        return jsonify({
            "status": "success",
            "harvest_prediction": result
        })

    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
if __name__ == "__main__":
    app.run(debug=True)
