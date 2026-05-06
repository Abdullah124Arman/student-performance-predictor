# Author: Abdullah Arman
# Project: Student Performance Predictor
import requests

url = "http://10.203.11.90:5000/predict"

# Example student data (you can change these values)
payload = {
    "attendance": 70,
    "internal1": 18,
    "internal2": 17,
    "assignment": 7
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
