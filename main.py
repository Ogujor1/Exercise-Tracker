import requests
import os
from datetime import datetime

NUTRI_APP_ID = "d1206366"
NUTRI_APP_KEY = "f76ae3569c62350a95493d0757a1b7f0"
EX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
reply = input("Tell me what Exercise you did? ").title()

sheety_post_api = "https://api.sheety.co/9792953a555907ece274054bc76236e2/myWorkouts/workouts"


headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY,
    "Content-Type": "application/json"
}
ex_params = {
    "query": reply
}
now = datetime.today().now()
date = now.date().strftime("%d/%m/%Y")

time = now.time().strftime("%X")
response = requests.post(url=EX_END_POINT, json=ex_params, headers=headers)
duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']
exercise = response.json()['exercises'][0]['user_input']

workout = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,

    }
}

response = requests.post(url=sheety_post_api, json=workout)
print(response.json())