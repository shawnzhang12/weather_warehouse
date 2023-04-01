from django.urls import path
from . import views

urlpatterns = [
    # Add other URL patterns as necessary
    path("<str:time>/<str:params>/<str:location>", views.weather_data, name="weather_data"),
]