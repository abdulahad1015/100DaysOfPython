import os

import requests
from datetime import *

# os.environ["APP_ID"]="43e92ef1"
# os.environ["APP_KEY"]="741ef8509fddb3850ced768eb066dba1"
# print(os.environ.get("APP_ID"))
APP_ID = "43e92ef1"
APP_KEY = "741ef8509fddb3850ced768eb066dba1"
date = datetime.now()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
sheety_url = "https://api.sheety.co/25865526c7240d7293b60bb2829ae102/myWorkouts/workouts"
sheety_header = {
    "Content-Type": "application/json"
}
endpoint = "/v2/natural/exercise"
url = f"https://trackapi.nutritionix.com{endpoint}"
query = input("Enter exercises you have done today: ")
body = {
    "query": query,
}

response = requests.post(url=url, headers=headers, json=body)
for i in response.json()['exercises']:
    sheety_body = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%H:%M:%S"),
            "exercise": i['name'],
            "duration": i['duration_min'],
            "calories": i['nf_calories']
        }
    }
    sheety_response = requests.post(url=sheety_url, json=sheety_body, headers=sheety_header)
    print(sheety_response.json())
