
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': 'pie',
    },
    headers={'api-key': '41f74417-b15d-4dbb-b2c3-67511c6c3a2b'}
)
print(r.json())

