ALERT_THRESHOLD_C = 40.0

def check_alert(city, temperature):
    """Return True if the city's temperature triggers a weather alert."""
    return temperature >= ALERT_THRESHOLD_C

def get_weather_report(readings):
    """readings: dict of {city: temperature}
    Returns dict of {city: 'ALERT' or 'NORMAL'}"""
    return {
        city: 'ALERT' if check_alert(city, temp) else 'NORMAL'
        for city, temp in readings.items()
    }

if __name__ == '__main__':
    sample = {'Mumbai': 38.0, 'Nagpur': 41.5, 'Pune': 35.0}
    for city, status in get_weather_report(sample).items():
        print(f'{city}: {status}')