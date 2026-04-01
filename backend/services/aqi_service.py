import random

def get_aqi_data():
    return {
        "city": "Delhi",
        "AQI": random.randint(150, 400),
        "PM2.5": random.randint(80, 250),
        "PM10": random.randint(120, 300)
    }
