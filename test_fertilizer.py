
from ai_weather.fertilizer import recommend_fertilizer

result = recommend_fertilizer(
    n=40,
    p=20,
    k=25,
    ph=5.2,
    crop="Tomato"
)

print("\nFERTILIZER RECOMMENDATION")
print("-------------------------")

for key, value in result.items():
    print(key, ":", value)
