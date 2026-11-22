from ai_weather.agmarknet_price import get_market_prices, compare_markets

print("Fetching Karnataka Tomato market prices...")

result = get_market_prices("Karnataka", "Tomato")

print("\nMARKET PRICE RESULT")
print("-------------------")

if result["status"] == "success":

    comparison = compare_markets(result)

    if comparison["status"] == "success":

        print("Total markets:", comparison["total_markets"])

        print("\nBEST MARKET")
        print("Market:", comparison["best_market"].get("market"))
        print("District:", comparison["best_market"].get("district"))
        print("Modal price:", comparison["best_market"].get("modal_price"))

    else:
        print(comparison["message"])

else:
    print("API Error:", result["message"])