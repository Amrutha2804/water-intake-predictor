# Water Intake Predictor

A ML-powered REST API that predicts daily water intake based on temperature, weight, and exercise duration.

## Run locally
pip install -r requirements.txt
uvicorn app.main:app --reload

## API
POST /predict
{
  "temperature": 29,
  "weight_kg": 72,
  "exercise_minutes": 40
}