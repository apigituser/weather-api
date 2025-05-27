import requests
import json
import os
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

@app.route("/<location>", methods=['GET'])
def weatherData(location):
    load_dotenv(dotenv_path="key.env")

    key = os.getenv('KEY')
    date1 = "2025-05-30"
    query = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}?key={key}"
    response = requests.get(query)

    with open("WEATHER_DATA.json", "w") as file:
        data = response.json()
        json.dump(data, file)
    return data