import requests

response = requests.get('https://flights-api.buraky.workers.dev/')

print(response.status_code)

print("\n\n")

check_content_type = response.headers['Content-Type']

print(check_content_type)

print("\n\n")

print(response.json())

