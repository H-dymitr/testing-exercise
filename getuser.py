import requests

url = "https://reqres.in/api/users/4"
response = requests.get(url)

print(response.status_code)
print(response.json())