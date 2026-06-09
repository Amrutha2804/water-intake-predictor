from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    temperature: float = Field(..., ge=0, le=60, description="Temperature in Celsius")
    weight_kg: float = Field(..., ge=20, le=200, description="Body weight in kg")
    exercise_minutes: float = Field(..., ge=0, le=300, description="Exercise duration in minutes")
class PredictResponse(BaseModel):
    predicted_water_liters: float
    message: str
