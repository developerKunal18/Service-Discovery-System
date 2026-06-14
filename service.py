import requests

service_data = {
    "service_name":
    "user-service",

    "address":
    "http://localhost:5001"
}

response = requests.post(
    "http://localhost:5000/register",
    json=service_data
)

print(response.json())
