# import os
# import streamlit as st
# import requests
# import pandas as pd

# st.set_page_config(
#     page_title="Customer Churn Prediction",
#     page_icon="📊",
#     layout="centered"
# )

# st.title("📊 Customer Churn Prediction")

# # AUTO API URL
# API_URL = os.getenv(
#     "API_URL",
#     "https://churn-api-30ag.onrender.com/predict"
# )

# # API helper function
# def predict_api(data):

#     try:
#         response = requests.post(
#             API_URL,
#             json=data,
#             timeout=30
#         )

#         if response.status_code == 200:
#             return response.json()

#         st.error(f"API Error: {response.status_code}")
#         return None

#     except requests.exceptions.RequestException as e:
#         st.error(f"Connection Error: {e}")
#         return None


# # Toggle mode
# mode = st.toggle("Switch to CSV Prediction Mode")

# # ---------------- Manual Prediction ----------------

# if not mode:

#     st.subheader("Manual Prediction")

#     # Basic Info
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     senior = st.selectbox("Senior Citizen", ["No", "Yes"])
#     partner = st.selectbox("Partner", ["No", "Yes"])
#     dependents = st.selectbox("Dependents", ["No", "Yes"])

#     # Core Features
#     tenure = st.slider("Tenure (months)", 0, 72, 12)

#     internet = st.selectbox(
#         "Internet Service",
#         ["DSL", "Fiber", "No"]
#     )

#     security = st.selectbox(
#         "Online Security",
#         ["No", "Yes"]
#     )

#     tech = st.selectbox(
#         "Tech Support",
#         ["No", "Yes"]
#     )

#     contract = st.selectbox(
#         "Contract",
#         ["Month-to-month", "One year", "Two year"]
#     )

#     paper = st.selectbox(
#         "Paperless Billing",
#         ["No", "Yes"]
#     )

#     monthly_charges = st.number_input(
#         "Monthly Charges",
#         0.0,
#         200.0,
#         70.0
#     )

#     # Derived feature
#     total_charges = tenure * monthly_charges

#     st.write(
#         f"💰 Total Charges (auto calculated): {total_charges:.2f}"
#     )

#     if st.button("Check Churn Risk"):

#         # Encoding
#         data = {

#             "tenure": tenure,

#             "Contract":
#             {
#                 "Month-to-month": 0,
#                 "One year": 1,
#                 "Two year": 2
#             }[contract],

#             "InternetService":
#             {
#                 "No": 0,
#                 "DSL": 1,
#                 "Fiber": 2
#             }[internet],

#             "OnlineSecurity":
#             1 if security == "Yes" else 0,

#             "TechSupport":
#             1 if tech == "Yes" else 0,

#             "MonthlyCharges":
#             monthly_charges,

#             "TotalCharges":
#             total_charges,

#             "PaperlessBilling":
#             1 if paper == "Yes" else 0,

#             "gender":
#             0 if gender == "Male" else 1,

#             "SeniorCitizen":
#             1 if senior == "Yes" else 0,

#             "Partner":
#             1 if partner == "Yes" else 0,

#             "Dependents":
#             1 if dependents == "Yes" else 0
#         }

#         result = predict_api(data)

#         if result:

#             prob = result["churn_probability"]

#             st.subheader(
#                 f"Churn Probability: {prob * 100:.2f}%"
#             )

#             # Risk Levels
#             if prob < 0.2:
#                 st.success("🟢 Low Churn Risk")

#             elif prob < 0.5:
#                 st.warning("🟡 Medium Churn Risk")

#             else:
#                 st.error("🔴 High Churn Risk")

#             st.progress(int(prob * 100))

# # ---------------- CSV Prediction ----------------

# else:

#     st.subheader("Batch Prediction using CSV")

#     file = st.file_uploader(
#         "Upload CSV file",
#         type=["csv"]
#     )

#     if file is not None:

#         df = pd.read_csv(file)

#         st.write("Uploaded Data")
#         st.dataframe(df.head())

#         predictions = []
#         probabilities = []

#         with st.spinner("Generating Predictions..."):

#             for _, row in df.iterrows():

#                 result = predict_api(
#                     row.to_dict()
#                 )

#                 if result:

#                     predictions.append(
#                         result["prediction"]
#                     )

#                     probabilities.append(
#                         result["churn_probability"]
#                     )

#                 else:
#                     predictions.append("Error")
#                     probabilities.append(None)

#         df["Prediction"] = predictions
#         df["Churn_Probability"] = probabilities

#         st.write("Prediction Results")
#         st.dataframe(df)

#         csv = df.to_csv(index=False)

#         st.download_button(
#             "⬇ Download Results",
#             csv,
#             "churn_predictions.csv",
#             "text/csv"
#         )
```python
import os
import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")

# ---------------- API URL ----------------

API_URL = os.getenv(
    "API_URL",
    "https://churn-api-30ag.onrender.com/predict"
)

# ---------------- API FUNCTION ----------------

def predict_api(data):

    try:

        response = requests.post(
            API_URL,
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()

        # Show detailed error
        st.error(response.text)
        return None

    except requests.exceptions.RequestException as e:

        st.error(f"Connection Error: {e}")
        return None


# ---------------- TOGGLE ----------------

mode = st.toggle("Switch to CSV Prediction Mode")

# ==================================================
# MANUAL PREDICTION
# ==================================================

if not mode:

    st.subheader("Manual Prediction")

    # ---------- BASIC INFO ----------

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    # ---------- CORE FEATURES ----------

    tenure = st.slider(
        "Tenure (months)",
        0,
        72,
        12
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber", "No"]
    )

    security = st.selectbox(
        "Online Security",
        ["No", "Yes"]
    )

    tech = st.selectbox(
        "Tech Support",
        ["No", "Yes"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paper = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        0.0,
        200.0,
        70.0
    )

    # ---------- DERIVED FEATURE ----------

    total_charges = float(
        tenure * monthly_charges
    )

    st.write(
        f"💰 Total Charges (auto calculated): {total_charges:.2f}"
    )

    # ---------- BUTTON ----------

    if st.button("Check Churn Risk"):

        # ---------- ENCODING ----------

        data = {

            "tenure": int(tenure),

            "Contract": int(
                {
                    "Month-to-month": 0,
                    "One year": 1,
                    "Two year": 2
                }[contract]
            ),

            "InternetService": int(
                {
                    "No": 0,
                    "DSL": 1,
                    "Fiber": 2
                }[internet]
            ),

            "OnlineSecurity": int(
                1 if security == "Yes" else 0
            ),

            "TechSupport": int(
                1 if tech == "Yes" else 0
            ),

            "MonthlyCharges": float(
                monthly_charges
            ),

            "TotalCharges": float(
                total_charges
            ),

            "PaperlessBilling": int(
                1 if paper == "Yes" else 0
            ),

            "gender": int(
                0 if gender == "Male" else 1
            ),

            "SeniorCitizen": int(
                1 if senior == "Yes" else 0
            ),

            "Partner": int(
                1 if partner == "Yes" else 0
            ),

            "Dependents": int(
                1 if dependents == "Yes" else 0
            )
        }

        # DEBUG JSON
        st.write(data)

        # ---------- API CALL ----------

        result = predict_api(data)

        # ---------- RESULT ----------

        if result:

            prob = result["churn_probability"]

            st.subheader(
                f"Churn Probability: {prob * 100:.2f}%"
            )

            # ---------- RISK LEVEL ----------

            if prob < 0.2:

                st.success(
                    "🟢 Low Churn Risk"
                )

            elif prob < 0.5:

                st.warning(
                    "🟡 Medium Churn Risk"
                )

            else:

                st.error(
                    "🔴 High Churn Risk"
                )

            # ---------- PROGRESS ----------

            st.progress(
                int(prob * 100)
            )

# ==================================================
# CSV PREDICTION
# ==================================================

else:

    st.subheader(
        "Batch Prediction using CSV"
    )

    file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.write("Uploaded Data")

        st.dataframe(df.head())

        predictions = []
        probabilities = []

        with st.spinner(
            "Generating Predictions..."
        ):

            for _, row in df.iterrows():

                # Convert row to proper types
                row_data = {

                    "tenure": int(row["tenure"]),

                    "Contract": int(
                        row["Contract"]
                    ),

                    "InternetService": int(
                        row["InternetService"]
                    ),

                    "OnlineSecurity": int(
                        row["OnlineSecurity"]
                    ),

                    "TechSupport": int(
                        row["TechSupport"]
                    ),

                    "MonthlyCharges": float(
                        row["MonthlyCharges"]
                    ),

                    "TotalCharges": float(
                        row["TotalCharges"]
                    ),

                    "PaperlessBilling": int(
                        row["PaperlessBilling"]
                    ),

                    "gender": int(
                        row["gender"]
                    ),

                    "SeniorCitizen": int(
                        row["SeniorCitizen"]
                    ),

                    "Partner": int(
                        row["Partner"]
                    ),

                    "Dependents": int(
                        row["Dependents"]
                    )
                }

                result = predict_api(
                    row_data
                )

                if result:

                    predictions.append(
                        result["prediction"]
                    )

                    probabilities.append(
                        result[
                            "churn_probability"
                        ]
                    )

                else:

                    predictions.append(
                        "Error"
                    )

                    probabilities.append(
                        None
                    )

        # ---------- OUTPUT ----------

        df["Prediction"] = predictions

        df["Churn_Probability"] = probabilities

        st.write("Prediction Results")

        st.dataframe(df)

        # ---------- DOWNLOAD ----------

        csv = df.to_csv(index=False)

        st.download_button(
            "⬇ Download Results",
            csv,
            "churn_predictions.csv",
            "text/csv"
        )
```
