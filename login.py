import requests

url = "https://reqres.in/api/login"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
