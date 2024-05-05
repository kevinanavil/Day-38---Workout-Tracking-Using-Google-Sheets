import requests
from datetime import datetime
import os
import dotenv

dotenv.load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
AUTH = os.getenv("AUTH")

syndigo_endpoint = os.getenv("syndigo_endpoint")
sheety_endpoint = os.getenv("sheety_endpoint")

#input_text = input("What u have done?: ")
input_text = "dance for 1 hour"

syndigo_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

syndigo_params = {
    "query": input_text
}

response = requests.post(url=syndigo_endpoint, json=syndigo_params, headers=syndigo_headers)
result = response.json()



sheety_headers = {
    "Authorization": AUTH
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#print(result)

for exercise in result["exercises"]:
    sheety_params = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
}

#print(sheety_params)

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
print(response.text)