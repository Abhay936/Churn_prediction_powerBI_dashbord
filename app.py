import os
import streamlit as st
import requests
import pandas as pd


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Customer Retention System",
    page_icon="📊",
    layout="centered"
)

st.title("📊 AI Customer Churn & Retention System")
st.caption(
    "AI-powered churn prediction with cost-optimized retention recommendations"
)


# ==================================================
# API URL
# ==================================================

API_URL = os.getenv(
    "API_URL",
    "https://churn-api-30ag.onrender.com/predict"
)


# ==================================================
# API FUNCTION
# ==================================================

def predict_api(data):

    try:

        response = requests.post(
            API_URL,
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()

        st.error(
            f"API Error {response.status_code}: {response.text}"
        )

        return None

    except requests.exceptions.RequestException as e:

        st.error(
            f"Connection Error: {e}"
        )

        return None


# ==================================================
# RETENTION STRATEGY ENGINE
# ==================================================

def generate_retention_strategy(
    churn_probability,
    monthly_charges,
    contract,
    internet,
    security,
    tech_support,
    tenure
):

    # ==================================================
    # LOW RISK
    # ==================================================

    if churn_probability < 0.30:

        return {
            "risk_level": "Low",
            "strategy": "No Incentive Required",
            "primary_action": "Normal Customer Engagement",
            "secondary_action": "Continue regular service monitoring",
            "discount_percent": 0,
            "discount_amount": 0,
            "reason": (
                "Customer has low churn probability. "
                "No financial incentive is required."
            )
        }


    # ==================================================
    # MEDIUM RISK
    # 30% - 55%
    # ==================================================

    elif churn_probability < 0.55:

        if security == "No":

            return {
                "risk_level": "Medium",
                "strategy": "Free Online Security Trial",
                "primary_action": (
                    "Offer free Online Security trial"
                ),
                "secondary_action": (
                    "Send personalized retention message"
                ),
                "discount_percent": 0,
                "discount_amount": 0,
                "reason": (
                    "Moderate churn risk. A service-based "
                    "benefit is preferred over a direct discount."
                )
            }

        elif tech_support == "No":

            return {
                "risk_level": "Medium",
                "strategy": "Free Tech Support Trial",
                "primary_action": (
                    "Offer temporary Tech Support"
                ),
                "secondary_action": (
                    "Follow up with customer"
                ),
                "discount_percent": 0,
                "discount_amount": 0,
                "reason": (
                    "Moderate churn risk. A service benefit "
                    "can improve perceived value without reducing revenue."
                )
            }

        else:

            return {
                "risk_level": "Medium",
                "strategy": "Customer Engagement",
                "primary_action": (
                    "Personalized customer engagement"
                ),
                "secondary_action": (
                    "Monitor churn risk"
                ),
                "discount_percent": 0,
                "discount_amount": 0,
                "reason": (
                    "Moderate churn risk but no strong "
                    "financial intervention is required."
                )
            }


    # ==================================================
    # ELEVATED RISK
    # 55% - 65%
    # ==================================================

    elif churn_probability < 0.65:

        if contract == "Month-to-month":

            return {
                "risk_level": "Elevated",
                "strategy": "Contract Upgrade",
                "primary_action": (
                    "Offer incentive for 1-year contract"
                ),
                "secondary_action": (
                    "Retention call + plan review"
                ),
                "discount_percent": 0,
                "discount_amount": 0,
                "reason": (
                    "Customer has elevated churn risk and "
                    "a month-to-month contract. A contract "
                    "upgrade is preferred before a direct discount."
                )
            }

        elif tech_support == "No":

            return {
                "risk_level": "Elevated",
                "strategy": "Service Upgrade",
                "primary_action": (
                    "Offer temporary Tech Support"
                ),
                "secondary_action": (
                    "Priority customer support"
                ),
                "discount_percent": 0,
                "discount_amount": 0,
                "reason": (
                    "A service-based intervention can address "
                    "customer experience without reducing revenue."
                )
            }

        else:

            discount_percent = 5

            discount_amount = (
                monthly_charges *
                discount_percent /
                100
            )

            return {
                "risk_level": "Elevated",
                "strategy": "Low-Cost Retention Discount",
                "primary_action": (
                    "Offer 5% retention discount"
                ),
                "secondary_action": (
                    "Personalized retention communication"
                ),
                "discount_percent": 5,
                "discount_amount": round(
                    discount_amount,
                    2
                ),
                "reason": (
                    "Customer has elevated churn risk. "
                    "A small targeted discount is used "
                    "to control retention expenditure."
                )
            }


    # ==================================================
    # HIGH RISK
    # 65% - 80%
    # ==================================================

    elif churn_probability < 0.80:

        if contract == "Month-to-month":

            discount_percent = 10

            discount_amount = (
                monthly_charges *
                discount_percent /
                100
            )

            return {
                "risk_level": "High",
                "strategy": "Contract Retention Offer",
                "primary_action": (
                    "Offer 10% discount with 1-year contract upgrade"
                ),
                "secondary_action": (
                    "Dedicated retention call + plan review"
                ),
                "discount_percent": 10,
                "discount_amount": round(
                    discount_amount,
                    2
                ),
                "reason": (
                    "Customer has high churn probability and "
                    "a month-to-month contract. A controlled "
                    "discount is combined with a longer-term "
                    "contract intervention."
                )
            }

        elif tech_support == "No":

            discount_percent = 10

            discount_amount = (
                monthly_charges *
                discount_percent /
                100
            )

            return {
                "risk_level": "High",
                "strategy": "Service + Discount Retention",
                "primary_action": (
                    "Offer 10% retention discount"
                ),
                "secondary_action": (
                    "Free Tech Support for 3 months"
                ),
                "discount_percent": 10,
                "discount_amount": round(
                    discount_amount,
                    2
                ),
                "reason": (
                    "High churn probability requires a stronger "
                    "retention intervention."
                )
            }

        else:

            discount_percent = 10

            discount_amount = (
                monthly_charges *
                discount_percent /
                100
            )

            return {
                "risk_level": "High",
                "strategy": "Targeted Retention Discount",
                "primary_action": (
                    "Offer 10% retention discount"
                ),
                "secondary_action": (
                    "Dedicated retention communication"
                ),
                "discount_percent": 10,
                "discount_amount": round(
                    discount_amount,
                    2
                ),
                "reason": (
                    "High churn probability justifies a "
                    "targeted financial incentive."
                )
            }


    # ==================================================
    # VERY HIGH RISK
    # >= 80%
    # ==================================================

    else:

        discount_percent = 15

        discount_amount = (
            monthly_charges *
            discount_percent /
            100
        )

        return {
            "risk_level": "Very High",
            "strategy": "Priority Retention Intervention",
            "primary_action": (
                "Dedicated retention call + 15% discount"
            ),
            "secondary_action": (
                "Contract upgrade + service enhancement"
            ),
            "discount_percent": 15,
            "discount_amount": round(
                discount_amount,
                2
            ),
            "reason": (
                "Very high churn probability requires an "
                "immediate targeted retention intervention. "
                "The maximum discount is reserved for this group."
            )
        }


# ==================================================
# DISPLAY RESULT
# ==================================================

def display_prediction_result(
    result,
    monthly_charges,
    contract,
    internet,
    security,
    tech_support,
    tenure
):

    if not result:
        return


    prediction = result.get(
        "prediction"
    )

    prob = float(
        result.get(
            "churn_probability",
            0
        )
    )


    # ==================================================
    # CHURN PREDICTION
    # ==================================================

    st.subheader(
        "📈 Churn Prediction"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Churn Probability",
            f"{prob * 100:.2f}%"
        )

    with col2:

        st.metric(
            "Prediction",
            str(prediction)
        )


    # ==================================================
    # RISK DISPLAY
    # ==================================================

    if prob < 0.30:

        st.success(
            "🟢 Low Churn Risk"
        )

    elif prob < 0.55:

        st.warning(
            "🟡 Medium Churn Risk"
        )

    elif prob < 0.65:

        st.warning(
            "🟠 Elevated Churn Risk"
        )

    elif prob < 0.80:

        st.error(
            "🔴 High Churn Risk"
        )

    else:

        st.error(
            "🚨 Very High Churn Risk"
        )


    # ==================================================
    # PROGRESS BAR
    # ==================================================

    st.progress(
        min(
            max(
                int(prob * 100),
                0
            ),
            100
        )
    )


    # ==================================================
    # RETENTION STRATEGY
    # ==================================================

    strategy = generate_retention_strategy(

        churn_probability=prob,

        monthly_charges=monthly_charges,

        contract=contract,

        internet=internet,

        security=security,

        tech_support=tech_support,

        tenure=tenure
    )


    st.subheader(
        "🎯 Recommended Retention Strategy"
    )


    st.info(
        f"**{strategy['strategy']}**"
    )


    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risk Level",
            strategy["risk_level"]
        )

    with col2:

        st.metric(
            "Recommended Discount",
            f"{strategy['discount_percent']}%"
        )


    # ==================================================
    # ACTIONS
    # ==================================================

    st.markdown(
        "### 🎯 Primary Action"
    )

    st.write(
        strategy["primary_action"]
    )


    st.markdown(
        "### 🔄 Secondary Action"
    )

    st.write(
        strategy["secondary_action"]
    )


    # ==================================================
    # DISCOUNT COST
    # ==================================================

    if strategy["discount_percent"] > 0:

        st.warning(
            f"💰 Estimated Monthly Discount Cost: "
            f"₹{strategy['discount_amount']:.2f}"
        )

    else:

        st.success(
            "💰 No direct discount cost required"
        )


    # ==================================================
    # REASON
    # ==================================================

    with st.expander(
        "Why was this strategy recommended?"
    ):

        st.write(
            strategy["reason"]
        )


    # ==================================================
    # BUSINESS INSIGHT
    # ==================================================

    st.subheader(
        "💡 Business Insight"
    )

    if strategy["discount_percent"] == 0:

        st.write(
            "The system selected a non-discount intervention "
            "to reduce unnecessary retention expenditure."
        )

    else:

        st.write(
            "The system recommends a targeted discount because "
            "the customer's churn probability is high enough "
            "to justify financial intervention."
        )


# ==================================================
# MODE TOGGLE
# ==================================================

mode = st.toggle(
    "Switch to CSV Prediction Mode"
)


# ==================================================
# MANUAL PREDICTION
# ==================================================

if not mode:

    st.subheader(
        "👤 Manual Prediction"
    )


    # ==================================================
    # BASIC INFORMATION
    # ==================================================

    st.markdown(
        "### Basic Information"
    )


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


    # ==================================================
    # SERVICE INFORMATION
    # ==================================================

    st.markdown(
        "### Customer & Service Information"
    )


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
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


    paper = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )


    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )


    # ==================================================
    # TOTAL CHARGES
    # ==================================================

    total_charges = float(
        tenure *
        monthly_charges
    )


    st.info(
        f"💰 Estimated Total Charges: "
        f"₹{total_charges:.2f}"
    )


    # ==================================================
    # PREDICTION BUTTON
    # ==================================================

    if st.button(
        "🔍 Check Churn Risk",
        use_container_width=True
    ):

        data = {

            "tenure": int(
                tenure
            ),

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
                1 if security == "Yes"
                else 0
            ),

            "TechSupport": int(
                1 if tech == "Yes"
                else 0
            ),

            "MonthlyCharges": float(
                monthly_charges
            ),

            "TotalCharges": float(
                total_charges
            ),

            "PaperlessBilling": int(
                1 if paper == "Yes"
                else 0
            ),

            "gender": int(
                0 if gender == "Male"
                else 1
            ),

            "SeniorCitizen": int(
                1 if senior == "Yes"
                else 0
            ),

            "Partner": int(
                1 if partner == "Yes"
                else 0
            ),

            "Dependents": int(
                1 if dependents == "Yes"
                else 0
            )
        }


        with st.expander(
            "🔧 View API Request"
        ):

            st.json(
                data
            )


        with st.spinner(
            "Analyzing customer..."
        ):

            result = predict_api(
                data
            )


        display_prediction_result(

            result,

            monthly_charges,

            contract,

            internet,

            security,

            tech,

            tenure
        )


# ==================================================
# CSV PREDICTION
# ==================================================

else:

    st.subheader(
        "📂 Batch Prediction using CSV"
    )

    st.write(
        "Upload a CSV containing the required "
        "customer features."
    )


    file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )


    if file is not None:

        try:

            df = pd.read_csv(
                file
            )

        except Exception as e:

            st.error(
                f"Unable to read CSV: {e}"
            )

            st.stop()


        st.write(
            "### Uploaded Data"
        )

        st.dataframe(
            df.head(),
            use_container_width=True
        )


        # ==================================================
        # REQUIRED COLUMNS
        # ==================================================

        required_columns = [

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


        missing_columns = [

            column

            for column in required_columns

            if column not in df.columns
        ]


        if missing_columns:

            st.error(
                "Missing required columns: "
                + ", ".join(
                    missing_columns
                )
            )

            st.stop()


        # ==================================================
        # RESULT LISTS
        # ==================================================

        predictions = []

        probabilities = []

        risk_levels = []

        strategies = []

        primary_actions = []

        secondary_actions = []

        discounts = []

        discount_costs = []


        # ==================================================
        # BATCH PREDICTION
        # ==================================================

        with st.spinner(
            "Generating predictions and retention strategies..."
        ):

            for _, row in df.iterrows():

                row_data = {

                    "tenure": int(
                        row["tenure"]
                    ),

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

                    probability = float(
                        result.get(
                            "churn_probability",
                            0
                        )
                    )


                    prediction = result.get(
                        "prediction",
                        "Unknown"
                    )


                    contract_value = {

                        0: "Month-to-month",
                        1: "One year",
                        2: "Two year"

                    }.get(
                        int(row["Contract"]),
                        "Unknown"
                    )


                    internet_value = {

                        0: "No",
                        1: "DSL",
                        2: "Fiber"

                    }.get(
                        int(row["InternetService"]),
                        "Unknown"
                    )


                    security_value = (

                        "Yes"

                        if int(
                            row["OnlineSecurity"]
                        ) == 1

                        else "No"
                    )


                    tech_value = (

                        "Yes"

                        if int(
                            row["TechSupport"]
                        ) == 1

                        else "No"
                    )


                    strategy = generate_retention_strategy(

                        probability,

                        float(
                            row["MonthlyCharges"]
                        ),

                        contract_value,

                        internet_value,

                        security_value,

                        tech_value,

                        int(
                            row["tenure"]
                        )
                    )


                    predictions.append(
                        prediction
                    )

                    probabilities.append(
                        round(
                            probability,
                            4
                        )
                    )

                    risk_levels.append(
                        strategy["risk_level"]
                    )

                    strategies.append(
                        strategy["strategy"]
                    )

                    primary_actions.append(
                        strategy["primary_action"]
                    )

                    secondary_actions.append(
                        strategy["secondary_action"]
                    )

                    discounts.append(
                        strategy["discount_percent"]
                    )

                    discount_costs.append(
                        strategy["discount_amount"]
                    )


                else:

                    predictions.append(
                        "Error"
                    )

                    probabilities.append(
                        None
                    )

                    risk_levels.append(
                        "Error"
                    )

                    strategies.append(
                        "Error"
                    )

                    primary_actions.append(
                        "Error"
                    )

                    secondary_actions.append(
                        "Error"
                    )

                    discounts.append(
                        None
                    )

                    discount_costs.append(
                        None
                    )


        # ==================================================
        # ADD RESULTS
        # ==================================================

        df["Prediction"] = predictions

        df["Churn_Probability"] = probabilities

        df["Risk_Level"] = risk_levels

        df["Retention_Strategy"] = strategies

        df["Primary_Action"] = primary_actions

        df["Secondary_Action"] = secondary_actions

        df["Recommended_Discount"] = discounts

        df["Estimated_Discount_Cost"] = discount_costs


        # ==================================================
        # RESULTS
        # ==================================================

        st.write(
            "### 🎯 Prediction & Retention Results"
        )

        st.dataframe(
            df,
            use_container_width=True
        )


        # ==================================================
        # BUSINESS SUMMARY
        # ==================================================

        st.subheader(
            "📊 Retention Cost Summary"
        )


        valid_probabilities = pd.to_numeric(
            df["Churn_Probability"],
            errors="coerce"
        )


        valid_discount_costs = pd.to_numeric(
            df["Estimated_Discount_Cost"],
            errors="coerce"
        )


        total_discount_cost = (
            valid_discount_costs
            .fillna(0)
            .sum()
        )


        high_risk_customers = (
            valid_probabilities
            .fillna(0)
            >= 0.65
        ).sum()


        customers_with_discount = (
            pd.to_numeric(
                df["Recommended_Discount"],
                errors="coerce"
            )
            .fillna(0)
            > 0
        ).sum()


        non_discount_actions = (

            (
                pd.to_numeric(
                    df["Recommended_Discount"],
                    errors="coerce"
                )
                .fillna(0)
                == 0
            )

            &

            (
                valid_probabilities
                .fillna(0)
                >= 0.30
            )

        ).sum()


        # ==================================================
        # METRICS
        # ==================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Total Customers",
                len(df)
            )


        with col2:

            st.metric(
                "High-Risk Customers",
                int(
                    high_risk_customers
                )
            )


        with col3:

            st.metric(
                "Estimated Discount Cost",
                f"₹{total_discount_cost:.2f}"
            )


        st.success(
            f"{int(non_discount_actions)} "
            "at-risk customers received a non-discount intervention."
        )


        st.info(
            f"{int(customers_with_discount)} "
            "customers received a financial discount recommendation."
        )


        # ==================================================
        # DOWNLOAD
        # ==================================================

        csv = df.to_csv(
            index=False
        )


        st.download_button(

            label="⬇ Download Prediction & Retention Results",

            data=csv,

            file_name="churn_retention_predictions.csv",

            mime="text/csv",

            use_container_width=True
        )

