from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
import joblib
import pandas as pd
import os

app = FastAPI(
    title="Water Intake Predictor",
    description="Predicts daily water intake based on temperature, weight and exercise.",
    version="1.0.0"
)

MODEL_PATH = "model/water_model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run model.py first.")
    return joblib.load(MODEL_PATH)

@app.get("/")
def root():
    return {"status": "running", "message": "Water Intake Predictor API is live!"}

@app.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    try:
        model = load_model()
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))

    input_df = pd.DataFrame([{
        "temperature": data.temperature,
        "weight_kg": data.weight_kg,
        "exercise_minutes": data.exercise_minutes
    }])

    prediction = model.predict(input_df)[0]
    prediction = round(float(prediction), 2)

    return PredictResponse(
        predicted_water_liters=prediction,
        message=f"You should drink approximately {prediction} liters of water today."
    )