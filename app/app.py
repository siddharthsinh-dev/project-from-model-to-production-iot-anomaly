from fastapi import FastAPI
import joblib
import numpy as np
import json

app = FastAPI()

# load model
model = joblib.load("artifacts/model.joblib")

# load meta info
with open("artifacts/meta.json", "r") as f:
    meta = json.load(f)


@app.get("/")
def home():
    return {"message": "IoT Anomaly Detection API is running"}


@app.post("/predict")
def predict(data: dict):
    temp = data["temperature"]
    hum = data["humidity"]
    sound = data["sound_volume"]

    X = np.array([[temp, hum, sound]])

    score = -model.score_samples(X)[0]

    is_anomaly = 1 if score > 0.6 else 0

    return {
        "anomaly_score": float(score),
        "is_anomaly": is_anomaly,
        "model_info": meta
    }