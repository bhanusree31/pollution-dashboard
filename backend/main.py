from fastapi import FastAPI
from services.aqi_service import get_aqi_data
from services.prediction_service import predict_aqi
from services.source_service import identify_sources
from services.recommendation_service import get_recommendations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Pollution Dashboard Running 🚀"}

@app.get("/aqi/current")
def current_aqi():
    return get_aqi_data()

@app.get("/aqi/predict")
def forecast():
    return predict_aqi()

@app.get("/sources")
def sources():
    return identify_sources()

@app.get("/recommendations")
def recommendations():
    return get_recommendations()
