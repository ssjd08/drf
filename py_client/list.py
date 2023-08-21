import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter your username:")
password = getpass()
auth_res = requests.post(auth_endpoint, json={"username":username, "password":password})
print(auth_res.json())

if auth_res.status_code == 200:
    token = auth_res.json()['token']
    headers = {
        "Authorization": f"Ssjd {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())