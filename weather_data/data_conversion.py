import pandas as pd

def convert_long_to_wide(long_data):
    wide_data = long_data.pivot_table(index=["location_id", "timestamp"], columns="parameter", values="value").reset_index()
    return wide_data


def convert_wide_to_long(wide_data):
    long_data = wide_data.melt(id_vars=["location_id", "timestamp"], var_name="parameter", value_name="value")
    return long_data


def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32


def celsius_to_kelvin(celsius_temp):
    return celsius_temp + 273.15


def convert_temperature(temp, unit):
    if unit == 'C':
        return temp
    elif unit == 'F':
        return celsius_to_fahrenheit(temp)
    elif unit == 'K':
        return celsius_to_kelvin(temp)
    else:
        raise ValueError("Invalid temperature unit")
    

def ms_to_bft(ms_wind_speed):
    if ms_wind_speed < 0.3:
        return 0
    elif ms_wind_speed < 1.6:
        return 1
    elif ms_wind_speed < 3.4:
        return 2
    #TODO: The rest here
    else:
        return 12


def ms_to_kmh(ms_wind_speed):
    return ms_wind_speed * 3.6


def ms_to_kn(ms_wind_speed):
    return ms_wind_speed * 1.94384


def convert_wind_speed(speed, unit):
    if unit == 'ms':
        return speed
    elif unit == 'bft':
        return ms_to_bft(speed)
    elif unit == 'kmh':
        return ms_to_kmh(speed)
    elif unit == 'kn':
        return ms_to_kn(speed)
    else:
        raise ValueError("Invalid wind speed unit")