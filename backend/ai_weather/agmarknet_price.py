
import requests


BASE_URL = "https://api.dharun.dev/v1/mandi"


def get_market_prices(state, commodity, district=None):
    """Fetch agricultural mandi prices."""

    params = {
        "state": state,
        "commodity": commodity
    }

    if district:
        params["district"] = district

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        return {
            "status": "success",
            "data": result
        }

    except requests.RequestException as error:
        return {
            "status": "error",
            "message": str(error)
        }
def compare_markets(price_response):
    """Sort markets by modal price, highest first."""

    if price_response.get("status") != "success":
        return price_response

    markets = price_response.get("data", {}).get("data", [])

    if not markets:
        return {
            "status": "error",
            "message": "No market price data available"
        }

    sorted_markets = sorted(
        markets,
        key=lambda market: market.get("modal_price", 0),
        reverse=True
    )

    return {
        "status": "success",
        "total_markets": len(sorted_markets),
        "best_market": sorted_markets[0],
        "all_markets": sorted_markets
    }
