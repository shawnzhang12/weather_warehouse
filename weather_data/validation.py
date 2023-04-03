
import re

def is_valid_location_string(location_str):
    # Single point pattern
    single_point_pattern = r'^-?\d+(\.\d+)?,-?\d+(\.\d+)?$'

    # Point list pattern
    point_list_pattern = r'^(-?\d+(\.\d+)?,-?\d+(\.\d+)?\+)+-?\d+(\.\d+)?,-?\d+(\.\d+)?$'

    # Line pattern
    line_pattern = r'^-?\d+(\.\d+)?,-?\d+(\.\d+)?_-?\d+(\.\d+)?,-?\d+(\.\d+)?:\d+$'

    # Polyline pattern
    polyline_pattern = r'^(-?\d+(\.\d+)?,-?\d+(\.\d+)?_)+-?\d+(\.\d+)?,-?\d+(\.\d+)?:\d+(\+-?\d+(\.\d+)?,-?\d+(\.\d+)?:\d+)*$'

    # Rectangle fixed number of points pattern
    rectangle_fixed_points_pattern = r'^-?\d+(\.\d+)?,-?\d+(\.\d+)?_-?\d+(\.\d+)?,-?\d+(\.\d+)?:\d+x\d+$'

    # Rectangle fixed resolution pattern
    rectangle_fixed_resolution_pattern = r'^-?\d+(\.\d+)?,-?\d+(\.\d+)?_-?\d+(\.\d+)?,-?\d+(\.\d+)?:-?\d+(\.\d+)?,-?\d+(\.\d+)?$'

    patterns = [
        single_point_pattern,
        point_list_pattern,
        line_pattern,
        polyline_pattern,
        rectangle_fixed_points_pattern,
        rectangle_fixed_resolution_pattern,
    ]

    for i, pattern in enumerate(patterns):
        if re.match(pattern, location_str):
            return True, i

    return False, -1


def is_valid_time_string(time_str):
    # Single point UTC pattern
    single_point_utc_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}Z$'

    # Single point local time pattern
    single_point_local_time_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}([+-]\d{2}:\d{2})?$'

    # Time period fixed length pattern
    time_period_fixed_length_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}ZP(([1-9]\d*[YMWD])|((T[1-9]\d*[HMS])?))+:P(([1-9]\d*[YMWD])|((T[1-9]\d*[HMS])?))+$'

    # Time period fixed end pattern
    time_period_fixed_end_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z--\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z:P(([1-9]\d*[YMWD])|((T[1-9]\d*[HMS])?))+$'

    # Comma-separated list pattern
    comma_separated_list_pattern = r'^(\d{4}-\d{2}-\d{2}T\d{2}(Z|[+-]\d{2}:\d{2})?,)+(\d{4}-\d{2}-\d{2}T\d{2}(Z|[+-]\d{2}:\d{2})?|(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}ZP(([1-9]\d*[YMWD])|((T[1-9]\d*[HMS])?))+:P(([1-9]\d*[YMWD])|((T[1-9]\d*[HMS])?))+)?)$'

    patterns = [
        single_point_utc_pattern,
        single_point_local_time_pattern,
        time_period_fixed_length_pattern,
        time_period_fixed_end_pattern,
        comma_separated_list_pattern,
    ]

    for i, pattern in enumerate(patterns):
        if re.match(pattern, time_str):
            return True, i

    return False, -1


def is_valid_api_parameters(api_params):
    # Define patterns for each parameter
    patterns = [
        r'^wind_speed_10m:ms$',
        r'^wind_dir_10m:d$',
        r'^wind_gusts_10m_1h:(ms|bft|km/h|kn)$',
        r'^wind_gusts_10m_24h:(ms|bft|km/h|kn)$',
        r'^t_2m:(C|K|F)$',
        r'^t_max_2m_24h:(C|K|F)$',
        r'^t_min_2m_24h:(C|K|F)$',
        r'^msl_pressure:(hPa|Pa)$',
        r'^precip_1h:mm$',
        r'^precip_24h:mm$',
        r'^weather_symbol_1h:idx$',
        r'^weather_symbol_24h:idx$',
        r'^uv:idx$',
        r'^sunrise:sql$',
        r'^sunset:sql$',
    ]

    # Split the input string by commas
    params_list = api_params.split(',')

    # Check each parameter individually
    for param in params_list:
        valid_param = False
        for pattern in patterns:
            if re.match(pattern, param):
                valid_param = True
                break

        if not valid_param:
            return False

    return True