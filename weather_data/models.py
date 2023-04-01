from django.db import models
from django.utils.translation import gettext_lazy as _

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Landing(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    wind_speed_10m_ms = models.FloatField(null=True, blank=True)
    wind_dir_10_d = models.FloatField(null=True, blank=True)
    wind_gusts_10m_1h_ms = models.FloatField(null=True, blank=True)
    wind_gusts_10m_24h_ms = models.FloatField(null=True, blank=True)
    t_2m_C = models.FloatField(null=True, blank=True)
    t_max_2m_24h_C = models.FloatField(null=True, blank=True)
    t_min_2m_24h_C = models.FloatField(null=True, blank=True)
    msl_pressure_hPa = models.FloatField(null=True, blank=True)
    precip_1h_mm = models.FloatField(null=True, blank=True)
    precip_24h_mm = models.FloatField(null=True, blank=True)
    weather_symbol_1h_idx = models.IntegerField(null=True, blank=True)
    weather_symbol_24h_idx = models.IntegerField(null=True, blank=True)
    uv_idx = models.FloatField(null=True, blank=True)
    sunrise = models.DateTimeField(null=True, blank=True)
    sunset = models.DateTimeField(null=True, blank=True)
    

class LongTemperature(models.Model):
    class TemperatureUnit(models.TextChoices):
        CELSIUS = 'C', _('Celsius')
        FAHRENHEIT = 'F', _('Fahrenheit')
        KELVIN = 'K', _('Kelvin')

    class TempType(models.TextChoices):
        INSTANTANEOUS = 'INST', _('Instantaneous')
        PREV_24H_MAX = 'MAX24', _('Previous 24-hour Max')
        PREV_24H_MIN = 'MIN24', _('Previous 24-hour Min')

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    temp_unit = models.CharField(max_length=2, choices=TemperatureUnit.choices)
    temp_type = models.CharField(max_length=5, choices=TempType.choices)


class WideTemperature(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temp_inst_celsius = models.FloatField(null=True, blank=True)
    temp_inst_fahrenheit = models.FloatField(null=True, blank=True)
    temp_inst_kelvin = models.FloatField(null=True, blank=True)

    temp_max24_celsius = models.FloatField(null=True, blank=True)
    temp_max24_fahrenheit = models.FloatField(null=True, blank=True)
    temp_max24_kelvin = models.FloatField(null=True, blank=True)

    temp_min24_celsius = models.FloatField(null=True, blank=True)
    temp_min24_fahrenheit = models.FloatField(null=True, blank=True)
    temp_min24_kelvin = models.FloatField(null=True, blank=True)


class LongWind(models.Model):
    class WindUnit(models.TextChoices):
        BEAUFORT = 'BFT', _('Beaufort')
        KILOMETERS = 'KMH', _('Kilometers/hour')
        KNOTS = 'KN', _('Knots')
        METERS = 'MS', _('Meters/second')
        DEGREES = 'DEG', _('Degrees')
    class WindType(models.TextChoices):
        SPEED = 'SPEED', _('Instantaneous wind Speed at 10m above ground')
        DIRECTION = 'DIR', _('Instantaneous wind direction at 10m above ground in degrees')
        GUST_1 = 'GUST1', _('Wind gusts in 10 m in the previous 1h')
        GUST_24 = 'GUST24', _('Wind gusts in 10 m in the previous 24h')

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    wind_unit = models.CharField(max_length=3, choices=WindUnit.choices)
    wind_type = models.CharField(max_length=6, choices=WindType.choices)
    wind_speed_10m_ms = models.FloatField(null=True, blank=True)
    wind_dir_10_d = models.FloatField(null=True, blank=True)
    wind_gusts_10m_1h_ms = models.FloatField(null=True, blank=True)
    wind_gusts_10m_24h_ms = models.FloatField(null=True, blank=True)


class WideWind(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    wind_speed_10m_ms = models.FloatField(null=True, blank=True)
    wind_dir_10_d = models.FloatField(null=True, blank=True)

    wind_gusts_10m_1h_ms = models.FloatField()
    wind_gusts_10m_1h_bft = models.FloatField()
    wind_gusts_10m_1h_kmh = models.FloatField()
    wind_gusts_10m_1h_kn = models.FloatField()

    wind_gusts_10m_24h_ms = models.FloatField()
    wind_gusts_10m_24h_bft = models.FloatField()
    wind_gusts_10m_24h_kmh = models.FloatField()
    wind_gusts_10m_24h_kn = models.FloatField()


class WideOther(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    msl_pressure_hPa = models.FloatField(null=True, blank=True)
    precip_1h_mm = models.FloatField(null=True, blank=True)
    precip_24h_mm = models.FloatField(null=True, blank=True)
    weather_symbol_1h_idx = models.IntegerField(null=True, blank=True)
    weather_symbol_24h_idx = models.IntegerField(null=True, blank=True)
    uv_idx = models.FloatField(null=True, blank=True)
    sunrise = models.DateTimeField(null=True, blank=True)
    sunset = models.DateTimeField(null=True, blank=True)
