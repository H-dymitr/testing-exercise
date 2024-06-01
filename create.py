import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "John",
    "job": "Developer"
}
response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())