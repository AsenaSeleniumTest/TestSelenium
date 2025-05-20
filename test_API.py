import requests
import pytest
BASE_URL = "https://api.football-data.org/"

response = requests.get(f"{BASE_URL}v4/matches")
jsonData = response.json()
print(jsonData)
assert response.status_code == 200

response2 = requests.post(f"{BASE_URL}v4/matches")
jsonData2 = response2.json()
print(response2.status_code)
assert response2.status_code == 405

response3 = requests.delete(f"{BASE_URL}v4/matches")
print(response3.status_code)
assert response3.status_code == 405