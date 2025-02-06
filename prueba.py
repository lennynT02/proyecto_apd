import requests
from collections import Counter

responses = []

for _ in range(100):
    response = requests.get("http://localhost")
    responses.append(response.text.strip())

count = Counter(responses)
print(count)
