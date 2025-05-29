from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis
import requests
import json
import os

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per hour"],
    storage_uri="memory://",
)

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.route("/gocrazy")
@limiter.exempt
def gocrazy():
    return "RAAAAAAARRRRRRRRRR"

@app.route("/check", methods=['GET'])
@limiter.limit("10 per minute")
def check():
    return "10 requests per minute ONLY"

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
