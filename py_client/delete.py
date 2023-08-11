import requests

x = input("plesae enter the product id you want to destroy:\n")
try:
    id = int(x)
except:
    id = None
    print("Invalid product id.")
    
if id:
    endpoint = f"http://localhost:8000/api/products/destroy/{id}/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)