import streamlit as st
import requests
import pandas as pd

st.title("Customer Churn Prediction")

mode = st.toggle("Switch to CSV Prediction Mode")

# ---------------- Manual Prediction ----------------

if not mode:

    st.subheader("Manual Prediction")

    # Basic Info
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

    # Core Features
    tenure = st.slider("Tenure (months)", 0, 72, 12)

    internet = st.selectbox("Internet Service", ["DSL","Fiber","No"])
    security = st.selectbox("Online Security", ["No","Yes"])
    tech = st.selectbox("Tech Support", ["No","Yes"])

    contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
    paper = st.selectbox("Paperless Billing", ["No","Yes"])

    monthly_charges = st.number_input("Monthly Charges",0.0,200.0,70.0)

    # Derived feature
    total_charges = tenure * monthly_charges
    st.write("Total Charges (auto):", total_charges)

    if st.button("Check"):

        # ✅ EXACT SAME ENCODING AS TRAINING
        data = {

        "tenure": tenure,
        "Contract": {"Month-to-month":0,"One year":1,"Two year":2}[contract],
        "InternetService": {"No":0,"DSL":1,"Fiber":2}[internet],
        "OnlineSecurity": 1 if security=="Yes" else 0,
        "TechSupport": 1 if tech=="Yes" else 0,

        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "PaperlessBilling": 1 if paper=="Yes" else 0,

        "gender": 0 if gender=="Male" else 1,
        "SeniorCitizen": 1 if senior=="Yes" else 0,
        "Partner": 1 if partner=="Yes" else 0,
        "Dependents": 1 if dependents=="Yes" else 0
        }

        url = "https://churn-api-30ag.onrender.com/predict"

        response = requests.post(url,json=data)
        result = response.json()

        prob = result["churn_probability"]

        st.write(f"Churn Probability: {prob*100:.2f}%")

        # 🎯 Better risk bands
        if prob < 0.2:
            st.success("Low Churn Risk")
        elif prob < 0.5:
            st.warning("Medium Churn Risk")
        else:
            st.error("High Churn Risk")

        # 🔥 Visual bar (nice UI)
        st.progress(int(prob*100))

# ---------------- CSV Prediction ----------------

else:

    st.subheader("Batch Prediction using CSV")

    file = st.file_uploader("Upload CSV file",type=["csv"])

    if file is not None:

        df = pd.read_csv(file)

        st.write("Uploaded Data")
        st.dataframe(df.head())

        url = "https://churn-api-30ag.onrender.com/predict"

        predictions=[]
        probabilities=[]

        for _,row in df.iterrows():

            response = requests.post(url,json=row.to_dict())
            result = response.json()

            predictions.append(result["prediction"])
            probabilities.append(result["churn_probability"])

        df["Prediction"]=predictions
        df["Churn_Probability"]=probabilities

        st.write("Prediction Results")
        st.dataframe(df)

        csv=df.to_csv(index=False)

        st.download_button(
            "Download Results",
            csv,
            "churn_predictions.csv",
            "text/csv"
        )