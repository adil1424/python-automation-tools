# api_automation.py
# Simple REST API automation example

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    print("API call successful!")
    data = response.json()
    print("Received items:", len(data))
else:
    print("API error:", response.status_code)
