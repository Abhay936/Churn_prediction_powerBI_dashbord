# 🚀 Customer Churn Prediction API

An end-to-end Machine Learning REST API for predicting customer churn using Logistic Regression.  
The model is deployed on the cloud using FastAPI and is publicly accessible.

---

## 🌐 Live API

🔗 Swagger Docs: https://churn-api-1-73me.onrender.com/docs      #/default/predict_predict_post 


---

## 📌 Project Overview

This project predicts whether a customer is likely to churn based on 19 encoded features.

The trained Logistic Regression model is served through a FastAPI-based REST API and deployed on the cloud.

---

## 🧠 Model Details

- Algorithm: Logistic Regression
- Training Environment:
  - Python 3.12
  - NumPy 2.0.2
  - Scikit-learn 1.6.1
- Input Features: 19 numeric features
- Output:
  - `prediction` (0 = No Churn, 1 = Churn)
  - `churn_probability`

---

## 📥 Example Request

```json
{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 1,
  "Dependents": 0,
  "tenure": 24,
  "PhoneService": 1,
  "MultipleLines": 1,
  "InternetService": 2,
  "OnlineSecurity": 0,
  "OnlineBackup": 1,
  "DeviceProtection": 0,
  "TechSupport": 0,
  "StreamingTV": 1,
  "StreamingMovies": 1,
  "Contract": 0,
  "PaperlessBilling": 1,
  "PaymentMethod": 2,
  "MonthlyCharges": 89.5,
  "TotalCharges": 2150.75
}

📤 Example Response
{
  "prediction": 0,
  "churn_probability": 0.4072
}

🛠 Tech Stack

Python
FastAPI
NumPy
Scikit-learn
Uvicorn
Git & GitHub
Render (Cloud Deployment)

📂 Project Structure
├── app.py
├── Churn_model.pkl
├── requirements.txt
├── runtime.txt
└── README.md

▶️ Run Locally
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app:app --reload

Open in browser:
http://127.0.0.1:8000/docs
