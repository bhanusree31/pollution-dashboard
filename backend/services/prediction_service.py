import random

def predict_aqi():
    future = [random.randint(200, 450) for _ in range(5)]

    return {
        "next_5_days": future,
        "trend": "Increasing "
    }
