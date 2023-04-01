import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from .models import Location, Landing, LongTemperature, LongWind, WideTemperature, WideWind, WideOther

load_dotenv(os.path.join("..", '.env'))

BASE_URL = "https://api.meteomatics.com"
USERNAME = os.environ.get("METEO_USER")
PASSWORD = os.environ.get("METEO_PASSWORD")

# Fix the time period, too many options for the time scope
# Example params: temperature_2m:C,precipitation_sum_1h:mm,wind_speed_10m:ms
def fetch_weather_data(location, start_time, params, end_time=""):
    if end_time == "":
        url = f"{BASE_URL}/{start_time}:PT1H/{location.latitude},{location.longitude}:{params}"
    else:
        url = f"{BASE_URL}/{start_time}--{end_time}:PT1H/{location.latitude},{location.longitude}:{params}"
    headers = {
        "Authorization": f"Basic {USERNAME}:{PASSWORD}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        if response.status_code == 400:
            raise Exception(f"Bad Request: {response.text}")
        elif response.status_code == 401:
            raise Exception(f"Unauthorized: Check your Meteomatics API credentials")
        elif response.status_code == 403:
            raise Exception(f"Forbidden: You do not have permission to access the requested resource")
        elif response.status_code == 404:
            raise Exception(f"Not Found: The requested resource could not be found")
        elif response.status_code >= 500:
            raise Exception(f"Internal Server Error: Meteomatics API encountered an error while processing the request")
        else:
            raise Exception(f"Error fetching weather data: {response.text}")
    
    data = response.json()
    return data

def store_landing_data(location, data):
    for entry in data['data']:
        timestamp = entry['validate']
        temperature, precipitation, wind_speed = entry['coordinates'][0]['values']

        Landing.objects.create(
            location=location,
            timestamp=timestamp,
            temperature=temperature,
            precipitation=precipitation,
            wind_speed=wind_speed
        )

def clean_validate_and_store_transformed_data(location):
    landing_data = Landing.objects.filter(location=location).values()

    # Clean and validate data (implement your cleaning and validation logic here)
    cleaned_data = landing_data

    # Store data in wide format
    for entry in cleaned_data:
        WideWeatherData.objects.create(
            location=location,
            timestamp=entry['timestamp'],
            temperature=entry['temperature'],
            precipitation=entry['precipitation'],
            wind_speed=entry['wind_speed']
        )

    # Store data in long format
    for entry in cleaned_data:
        LongWeatherData.objects.create(
            location=location,
            timestamp=entry['timestamp'],
            parameter='temperature',
            value=entry['temperature']
        )
        LongWeatherData.objects.create(
            location=location,
            timestamp=entry['timestamp'],
            parameter='precipitation',
            value=entry['precipitation']
        )
        LongWeatherData.objects.create(
            location=location,
            timestamp=entry['timestamp'],
            parameter='wind_speed',
            value=entry['wind_speed']
        )


def save_and_transform_data(location, raw_data):
    wide_data = []

    for entry in raw_data:
        timestamp = entry['timestamp']
        weather_data = entry['weather_data']

        # Save the raw data to the landing table
        landing_data = LandingWeatherData(
            location=location,
            timestamp=timestamp,
            raw_data=weather_data
        )
        landing_data.save()

        # Clean, validate, and store the transformed data
        wide_entry = clean_validate_and_store_transformed_data(location, timestamp, weather_data)
        wide_data.append(wide_entry)

    return wide_data


def save_data_to_long_temperature(location, timestamp, temperature_data):
    # Your implementation to save data to LongTemperature model
    pass

def save_data_to_long_wind(location, timestamp, wind_data):
    # Your implementation to save data to LongWind model
    pass

def save_data_to_wide_temperature(location, timestamp, wide_temperature_data):
    # Your implementation to save data to WideTemperature model
    pass

def save_data_to_wide_wind(location, timestamp, wide_wind_data):
    # Your implementation to save data to WideWind model
    pass

def save_data_to_wide_other(location, timestamp, wide_other_data):
    # Your implementation to save data to WideOther model
    pass