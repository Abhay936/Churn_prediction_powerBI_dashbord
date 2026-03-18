from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model + scaler
with open("Churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("Scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

feature_order = [
    "tenure",
    "Contract",
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "MonthlyCharges",
    "TotalCharges",
    "PaperlessBilling",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents"
]

@app.post("/predict")
def predict(data: dict):

    features = np.array([data[f] for f in feature_order]).reshape(1, -1)

    # 🔥 IMPORTANT FIX
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }