import requests

# Endpoint URL
url = 'http://127.0.0.1:8000/query/'

# Data to be sent
data = {'text': 'Arbués'}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print('Status Code:', response.status_code)
print('Response:', response.json())
