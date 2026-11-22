
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

BASE_URL = "https://api.ceda.ashoka.edu.in/v1/agmarknet"


def get_headers():
    api_key = os.getenv("CEDA_API_KEY")

    if not api_key:
        return None

    return {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }


def get_commodities():
    """Fetch available agricultural commodities."""

    headers = get_headers()
    if not headers:
        return {"error": "CEDA API key not found"}

    try:
        response = requests.get(
            f"{BASE_URL}/commodities",
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        result = response.json()
        commodities = result.get("output", {}).get("data", [])

        return {
            "status": "success",
            "total_commodities": len(commodities),
            "commodities": commodities
        }

    except requests.RequestException as error:
        return {"error": f"CEDA API request failed: {error}"}
    except ValueError:
        return {"error": "Invalid JSON response from CEDA"}


def get_geographies():
    """Fetch available states and districts."""

    headers = get_headers()
    if not headers:
        return {"error": "CEDA API key not found"}

    try:
        response = requests.get(
            f"{BASE_URL}/geographies",
            headers=headers,
            timeout=90
        )
        response.raise_for_status()

        result = response.json()
        data = result.get("output", result)
        geographies = data.get("geographies", [])

        return {
            "status": "success",
            "total_states": len(geographies),
            "geographies": geographies
        }

    except requests.RequestException as error:
        return {"error": f"CEDA API request failed: {error}"}
    except ValueError:
        return {"error": "Invalid JSON response from CEDA"}


def get_markets(commodity_id, state_id, district_id):
    """Fetch available markets."""

    headers = get_headers()
    if not headers:
        return {"error": "CEDA API key not found"}

    payload = {
        "commodity_id": commodity_id,
        "state_id": state_id,
        "district_id": district_id,
        "indicator": "price"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/markets",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        data = result.get("output", result)
        markets = data.get("data", [])

        return {
            "status": "success",
            "total_markets": len(markets),
            "markets": markets
        }

    except requests.RequestException as error:
        return {"error": f"CEDA API request failed: {error}"}
    except ValueError:
        return {"error": "Invalid JSON response from CEDA"}


def get_market_prices(commodity_id, state_id, district_ids, market_ids,
                      from_date, to_date):
    """Fetch agricultural market prices."""

    headers = get_headers()
    if not headers:
        return {"error": "CEDA API key not found"}

    payload = {
        "commodity_id": commodity_id,
        "state_id": state_id,
        "district_id": district_ids,
        "market_id": market_ids,
        "from_date": from_date,
        "to_date": to_date
    }

    try:
        response = requests.post(
            f"{BASE_URL}/prices",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        data = result.get("output", result)
        prices = data.get("data", [])

        return {
            "status": "success",
            "total_records": len(prices),
            "prices": prices
        }

    except requests.RequestException as error:
        return {"error": f"CEDA API request failed: {error}"}
    except ValueError:
        return {"error": "Invalid JSON response from CEDA"}


def summarize_market_prices(price_data):
    """Summarize the latest available market price."""

    if price_data.get("status") != "success":
        return {
            "error": price_data.get("error", "Unable to get price data")
        }

    prices = price_data.get("prices", [])

    if not prices:
        return {"error": "No market price records available"}

    latest = max(prices, key=lambda item: item["date"])

    return {
        "date": latest["date"],
        "minimum_price": latest["min_price"],
        "maximum_price": latest["max_price"],
        "modal_price": latest["modal_price"],
        "note": "Prices are based on the latest available CEDA record."
    }
