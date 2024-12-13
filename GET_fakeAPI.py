import requests
import json
head = {
    'acceopt' : 'text/plain'
}

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

response = requests.get(url,headers = head)
print(response.json())
print(response.status_code)
assert response.status_code == 200
data = response.json()
print(data[29])
