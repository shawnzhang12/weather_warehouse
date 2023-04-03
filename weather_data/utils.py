
# Return list of tuple of time ranges, if single time point then start and end are the same
def get_times(time, time_pattern):
    return NotImplementedError

# Return list of locations, use geodjango and postgis
def get_locations(location, location_pattern):
    return NotImplementedError

# Return dictionary with keys being parameter name, and values being the unit
def get_params():
    return NotImplementedError