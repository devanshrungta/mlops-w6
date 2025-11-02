from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Iris Prediction API", version="1.0")

# Load model
model = joblib.load("model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "Iris API is running!"}

@app.post("/predict")
def predict(data: IrisInput):
    X = pd.DataFrame([data.dict()])
    prediction = model.predict(X)[0]
    return {"prediction": str(prediction)}

