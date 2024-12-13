import data
import requests

head = {'Accept': 'text/plain',
        'Content-Type': 'application/json; v=1.0'
        }
reuest_payload = {
   "id": 150,
   "title": "john class",
   "dueDate": "2024-12-02T16:48:35.418Z",
   "completed": True
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=head,json=reuest_payload)
print(response.status_code)
print(response.json())
data = response.json()
print(data['id'])
assert response.status_code == 200
assert data['id'] == 150