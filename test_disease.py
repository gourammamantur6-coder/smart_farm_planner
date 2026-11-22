import requests

url = "http://127.0.0.1:5000/api/disease-detection"

image_path = r"C:\Users\kousa\Downloads\leaf.jpeg"

with open(image_path, "rb") as image:
    response = requests.post(
        url,
        files={"image": image}
    )

print(response.status_code)
print(response.json())