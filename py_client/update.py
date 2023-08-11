import requests


endpoint = "http://localhost:8000/api/products/update/2/"
data = {
    "title": "new title",
    "price" : 1
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())