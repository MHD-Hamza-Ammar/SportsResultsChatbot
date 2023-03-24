import requests
import json

url = "http://localhost:5005/webhooks/rest/webhook"
data = json.dumps({"sender": "user", "message": "hi"})

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=data, headers=headers)

print(response.json())