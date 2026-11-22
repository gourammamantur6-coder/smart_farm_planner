from ai_weather.market_price import get_commodities

print("Testing CEDA API...")

result = get_commodities()

print("\nCEDA COMMODITY LIST")
print("-------------------")
print("Status:", result.get("status", "failed"))
print("Total commodities:", result.get("total_commodities", 0))

for item in result.get("commodities", [])[:10]:
    print(item["commodity_id"], "-", item["commodity_name"])