import requests


endpoint = "http://localhost:8000/api/products/"
headers = {'Authorization': 'Ssjd 36f251d03fc0c9554d58f6e79b287845fcd521cf'}
data = {
    'title': 'Product 2',
    'price': 25,
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())