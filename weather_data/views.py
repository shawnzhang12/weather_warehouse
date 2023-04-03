from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.gis.geos import Polygon
from rest_framework.decorators import api_view
from .models import Location, Landing, LongTemperature, LongWind, WideWind, WideTemperature, LongOther
from .meteomatics import fetch_weather_data, store_landing_data
from .validation import is_valid_location_string, is_valid_time_string, is_valid_api_parameters
from .utils import get_times, get_locations, get_params
from .validators import is_valid_query
import pandas as pd


param_model_mapping={
        'wind_speed_10m': 'wind',
        'wind_dir_10m': 'wind',
        'wind_gusts_10m_1h': 'wind',
        'wind_gusts_10m_24h': 'wind',
        't_2m': 'temp',
        't_max_2m_24h': 'temp',
        't_min_2m_24h': 'temp',
        'msl_pressure': 'misc',
        'precip_1h': 'misc',
        'precip_24h': 'misc',
        'weather_symbol_1h': 'misc',
        'weather_symbol_24h': 'misc',
        'uv': 'misc',
        'sunrise': 'misc',
        'sunset': 'misc',
}

@api_view(['GET'])
def main_view(request, time, params, location):
    try:
        if not is_valid_query(time, params, location):
            return JsonResponse({'error': 'Invalid query. Check the weather warehouse documentation for proper usage.'}, status=400)
        
        time_check, time_pattern = is_valid_time_string(time)
        if not time_check: 
            return JsonResponse({'error': 'Invalid timerange format.'}, status=400)

        location_check, location_pattern = is_valid_location_string(location)
        if not location_check:
            return JsonResponse({'error': 'Invalid location format.'}, status=400)
        
        if not is_valid_api_parameters(params):
            return JsonResponse({'error': 'Invalid api parameters.'}, status=400)
 
        time_list = get_times(time, time_pattern)
        loc_list = get_locations(location, location_pattern)
        param_dict = get_params(params)

        query_conditions = Q()

        for start_time, end_time in time_list:
            for loc in loc_list:
                query_conditions |= Q(
                    location=loc,
                    timestamp__range=(start_time, end_time),
                )

        combined_df = pd.DataFrame()
        combined_df = pd.merge(temperature_df, wind_df, on=['location', 'timestamp'])

        for param, value in param_dict.items():
            table = param_model_mapping[param]
            if table == 'temp':
                temperature_data = WideTemperature.objects.filter(query_conditions).values(param + ":C")
                if not temperature_data.exists():  # Query Meteomatics API
                    temperature_data = fetch_weather_data(time, param + ":C", location)
                    store_landing_data(location, temperature_data)
                temperature_df = pd.DataFrame.from_records(temperature_data.values())
                combined_df = pd.merge(combined_df, temperature_df, on=['location', 'timestamp'])
                # TODO: if value is not Celsius, load into pandas or polar dataframe, apply conversion to column

            elif table == 'wind':
                # Extra check for value unit
                wind_data = WideWind.objects.filter(query_conditions).values(param + ":" + value)
                if not wind_data.exists():  # Query Meteomatics API
                    wind_data = fetch_weather_data(time, param + ":" + value, location)
                    store_landing_data(location, wind_data)
                wind_df = pd.DataFrame.from_records(wind_data.values())
                combined_df = pd.merge(combined_df, wind_df, on=['location', 'timestamp'])
                # TODO: if value is not ms or deg, load into pandas or polar dataframe, apply conversion to column

            else:
                misc_data = LongOther.objects.filter(query_conditions).values(param + ":" + value)
                if not misc_data.exists():  # Query Meteomatics API
                    misc_data = fetch_weather_data(time, param + ":" + value, location)
                    store_landing_data(location, misc_data)
                misc_df = pd.DataFrame.from_records(misc_data.values())
                combined_df = pd.merge(combined_df, misc_df, on=['location', 'timestamp'])

        return JsonResponse(combined_df.to_json(), status=200)
        
    except Exception:
        # If no specific parameters match, return an error message
        return JsonResponse({'error': 'Invalid parameters'}, status=400)