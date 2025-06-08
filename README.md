# Weather API
The weather-api takes the name of a location and returns weather data to the user

## Example Response
```
{
  "conditions": "Rain, Partially cloudy",
  "currenttemp": "73.8",
  "datetime": "2025-06-07",
  "description": "Partly cloudy throughout the day with rain in the morning and afternoon.",
  "latitude": "40.7146",
  "longitude": "-74.0071",
  "maxtemp": "76.9",
  "mintemp": "69.0",
  "sunrise": "05:25:08",
  "sunset": "20:25:16",
  "timezone": "America/New_York",
  "winddirection": "356.1",
  "windspeed": "5.8"
}
```
## Installation and Setup
1. Clone this repository
```
git clone https://github.com/apigituser/weather-api
```
2. Go to the weather-api directory and install requirements
```
pip install -r requirements.txt
```
3. Create a key.env file and write your visualcrossing key in it like below
```
KEY=Your_Key
```
4. Run the flask application using the command below
```
flask --app weather run
```
5. Open your browser and go to the URL
```
127.0.0.1:5000/<location>  // URL Format
127.0.0.1:5000/Shibuya     // Example Request
```

## Optional
Change the redis connection information as per your own environment in weather.py
```
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
```

## Roadmap.sh Project URL
Project link is available [here](https://roadmap.sh/projects/weather-api-wrapper-service)
