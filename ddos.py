import requests
import time

url = "http://localhost:8080/api/test"

for i in range(20):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Request {i + 1}: Success ({response.status_code}) - {response.text}")

        elif response.status_code == 429:
            print(f"Request {i + 1}: Rate Limited ({response.status_code}) - {response.json()}")

        else:
            print(f"Request {i + 1}: Unexpected Status ({response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Request {i + 1}: Failed - {e}")
