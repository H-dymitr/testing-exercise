import requests

url = "https://reqres.in/api/register"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())