import requests

# Define headers and request payload
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 10fab95099c3e3696dcaf6dbc3d308701fd066908d205a74adb5c5b00147a9da'
}

request_body = {
    "name": "Fr. Tushar Mehrotraaaa", 
    "email": "tushar_fr_mehrottrraaa@feiiil-pagac.test",
    "gender": "male",
    "status": "active"
}

# Post request to create a user
response = requests.post("https://gorest.co.in/public/v2/users", headers=headers, json=request_body)
print(response.json())
assert response.status_code == 201

# Extract and print the user ID
data = response.json()
print(data['id'])
reqid = data['id']

# Get request to retrieve the created user
response_get = requests.get(f"https://gorest.co.in/public/v2/users/{reqid}", headers=headers)
print(response_get.json())
