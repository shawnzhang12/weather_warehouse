from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from .models import Location, Landing
from .meteomatics import fetch_weather_data

@api_view(['GET'])
def main_view(request, location, timerange, *params):
    try:
        loc = Location.objects.get(pk=location)
        timerange = timerange.split("--")
        start_time = timerange[0]
        if len(timerange) == 2:
            end_time = timerange[1]

        start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
        end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")

        q = Q(location=loc) & Q(timestamp__gte=start_time) & Q(timestamp__lte=end_time)
    
        # Check if all parameter values for the given time range exist
        all_data_exists = True
        for param in params:
            #model_class = get_model_class_by_param(param)
            model_class = None
            if not model_class.objects.filter(q).exists():
                all_data_exists = False
                break
        
        if all_data_exists:
            # Retrieve and return data from the database
            pass
        else:
             # If data does not exist, fetch it from Meteomatics API
            params = "t_2m:C,precip_1h:mm,wind_speed_10m:ms"  # Replace with desired parameters
            fetched_data = fetch_weather_data(location, start_time, params)

            # Save fetched data to the database
            data = Landing(location=location, timestamp=start_time, **fetched_data)
            data.save()

            # Return fetched data
            response_data = {
                "location": {
                    "latitude": data.location.latitude,
                    "longitude": data.location.longitude,
                },
                "timestamp": data.timestamp,
                # Add other fields as necessary
            }

        return JsonResponse(response_data)
    except Exception:
        # If no specific parameters match, return an error message
        return JsonResponse({'error': 'Invalid parameters'}, status=400)



@api_view(["GET"])
def weather_data(request):
    if request.method == "GET":
        latitude = float(request.GET.get("latitude"))
        longitude = float(request.GET.get("longitude"))
        start_time = request.GET.get("start_time")
        end_time = request.GET.get("end_time")

        location, _ = Location.objects.get_or_create(latitude=latitude, longitude=longitude)

        # Check if data exists in the database
        existing_data = Landing.objects.filter(location=location, timestamp=start_time)

        if existing_data.exists():
            # If data exists, return it
            data = existing_data.first()
            response_data = {
                "location": {
                    "latitude": data.location.latitude,
                    "longitude": data.location.longitude,
                },
                "timestamp": data.timestamp,
                # Add other fields as necessary
            }
        else:
            # If data does not exist, fetch it from Meteomatics API
            params = "t_2m:C,precip_1h:mm,wind_speed_10m:ms"  # Replace with desired parameters
            fetched_data = fetch_weather_data(location, start_time, params)

            # Save fetched data to the database
            data = Landing(location=location, timestamp=start_time, **fetched_data)
            data.save()

            # Return fetched data
            response_data = {
                "location": {
                    "latitude": data.location.latitude,
                    "longitude": data.location.longitude,
                },
                "timestamp": data.timestamp,
                # Add other fields as necessary
            }

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Invalid request method"})