import json
import requests

url = "https://gorest.co.in/public/v2/users/6942850"

head = {'Authorization': 'Bearer 10fab95099c3e3696dcaf6dbc3d308701fd066908d205a74adb5c5b00147a9da'}

request_get = requests.get(url, headers=head)
print(request_get.status_code)
# print()
data = request_get.json()


assert request_get.status_code == 200
print(data['name'])
assert data['name'] == 'Kanak Khan'
