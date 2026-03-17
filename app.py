from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("Churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# ✅ Correct feature order (same as training)
feature_order = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "Contract",
    "PaperlessBilling",
    "MonthlyCharges",
    "TotalCharges"
]

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict(data: dict):

    # 🔥 IMPORTANT FIX
    features = np.array([data[f] for f in feature_order]).reshape(1, -1)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }