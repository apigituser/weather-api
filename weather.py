from dotenv import load_dotenv
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis, redis.exceptions
import requests, os

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per hour"],
    storage_uri="memory://",
)

try:
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    r.ping()
    print("Redis Connection Established")
except redis.exceptions.ConnectionError as e:
    print('Redis ConnectionError: Couldn\'t Connect To The Server\n')
    exit(1)
except Exception as internal_error:
    raise internal_error

@app.route("/<location>", methods=['GET'])
@limiter.limit("10 per minute")
def weatherData(location):
    if r.exists(location):
        redis_data = r.hgetall(location)
        return redis_data
    
    load_dotenv(dotenv_path="key.env")

    key = os.getenv('KEY')
    
    query = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={key}"
    response = requests.get(query)

    if response.status_code == 400:
        return {"400": "BadRequest"}
    elif response.status_code == 401:
        return {"401": "Unauthorized"}

    jsonData = response.json()

    days = jsonData['days'][0]
    data = {'timezone': jsonData['timezone'],
            'latitude': jsonData['latitude'],
            'longitude': jsonData['longitude'],
            'datetime': days['datetime'],
            'currenttemp': days['temp'],
            'mintemp': days['tempmin'],
            'maxtemp': days['tempmax'],
            'windspeed': days['windspeed'],
            'winddirection': days['winddir'],
            'conditions': days['conditions'],
            'description': days['description'],
            'sunrise': days['sunrise'],
            'sunset': days['sunset']
    }

    r.hset(location, mapping=data)
    r.expire(location, 120, nx=True)

    return data
