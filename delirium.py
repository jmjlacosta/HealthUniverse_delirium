import streamlit as st
import numpy as np

# Define the function to calculate the DRI
def calculate_delirium(psychosis, alcohol_abuse, dementia, weight_loss, neurological_disorders, 
                      depression, fluid_elect_disorder, chf, drug_abuse, mi, coagulopathy, cerebro_vascular, renal_failure, pulmonary_circulation):
    
    # Intercept for dri logistic model
    LP = 0
    
    # Linear predictor
    LP += 6 * psychosis
    LP += 6 * alcohol_abuse
    LP += 4 * dementia
    LP += 2 * weight_loss
    LP += 2 * neurological_disorders
    LP += 2 * depression
    LP += 2 * fluid_elect_disorder
    LP += 1 * chf
    LP += 1 * drug_abuse
    LP += 1 * mi
    LP += 1 * coagulopathy
    LP += 1 * cerebro_vascular
    LP += 1 * renal_failure
    LP += 1 * pulmonary_circulation

    # Logistic function for dri
    index = LP
    
    return index, LP

# Function to classify the risk based on DRI score
def classify_risk(LP):
    if LP >= 5:
        return "High Risk", "red"
    elif 2 <= LP < 5:
        return "Medium Risk", "orange"
    else:
        return "Low Risk", "green"

# Streamlit UI for DRI
st.title("Delirium Risk Index App")

# Add a brief description at the start
st.markdown("""
### Overview
The Delirium Risk Index (DRI) is a tool used to assess the likelihood of delirium in hospitalized patients based on key comorbidities. 
Each comorbidity is assigned a weight based on its contribution to the risk of delirium. These weights are derived by multiplying 
the regression coefficients from the logistic model by 5 and rounding to the nearest integer. The DRI score is then calculated by 
summing the weights of the selected comorbidities. Patients are classified into risk categories as follows:
- **Low Risk**: DRI score of 0-1
- **Medium Risk**: DRI score of 2-4
- **High Risk**: DRI score ≥ 5
""")

# Diagnosis section
st.header("Delirium Risk Indicators")
col1, col2 = st.columns(2)

# Define tooltips
diagnosis_tooltips = {
    "psychosis": "ICD10-CM: F20,F22,F23,F24,F25.9,F28,F29,F30.1,F30.2,F30.3,F30.4,F30.8,F31,F32,F33,F34.81,F34.89,F39,F44.89,F84.3",
    "alcohol_abuse": "ICD10-CM: F10",
    "dementia": "ICD10-CM: F01.50,F01.51,F02.80,F02.81,F03.90,G31.1",
    "weight_loss": "ICD10-CM: E40,E41,E43,E44.0,E44.1,E45,E46,R63.4,R63.6",
    "neurological_disorders": "ICD10-CM: G20,G35,G37.3,G91.0,R56.00,R47.01",
    "depression": "ICD10-CM: F32.9,F34.1,F43.21",
    "fluid_elect_disorder": "ICD10-CM: E86,E87.0,E87.2",
    "chf": "ICD10-CM: I50",
    "drug_abuse": "ICD10-CM: F11,F12,F13,F14,F15",
    "mi": "ICD10-CM: I21,I25.2",
    "coagulopathy": "ICD10-CM: D65,D68.9",
    "cerebro_vascular": "ICD10-CM: I60,I69",
    "renal_failure": "ICD10-CM: N18,N19",
    "pulmonary_circulation": "ICD10-CM: I26,I27",
}

with col1:
    psychosis = st.checkbox("Psychosis", help=diagnosis_tooltips["psychosis"])
    alcohol_abuse = st.checkbox("Alcohol Abuse", help=diagnosis_tooltips["alcohol_abuse"])
    dementia = st.checkbox("Dementia", help=diagnosis_tooltips["dementia"])
    weight_loss = st.checkbox("Weight Loss", help=diagnosis_tooltips["weight_loss"])
    neurological_disorders = st.checkbox("Neurological Disorders", help=diagnosis_tooltips["neurological_disorders"])
    depression = st.checkbox("Depression", help=diagnosis_tooltips["depression"])
    fluid_elect_disorder = st.checkbox("Fluid & Electrolyte Disorders", help=diagnosis_tooltips["fluid_elect_disorder"])
    
with col2:
    chf = st.checkbox("Congestive Heart Failure", help=diagnosis_tooltips["chf"])
    drug_abuse = st.checkbox("Drug Abuse", help=diagnosis_tooltips["drug_abuse"])
    mi = st.checkbox("Myocardial Infarction", help=diagnosis_tooltips["mi"])
    coagulopathy = st.checkbox("Coagulopathy", help=diagnosis_tooltips["coagulopathy"])
    cerebro_vascular = st.checkbox("Cerebrovascular Disease", help=diagnosis_tooltips["cerebro_vascular"])
    renal_failure = st.checkbox("Renal Failure", help=diagnosis_tooltips["renal_failure"])
    pulmonary_circulation = st.checkbox("Pulmonary Circulation Disease", help=diagnosis_tooltips["pulmonary_circulation"])

# Compute DRI score
if st.button("Calculate Delirium Risk Index"):
    index, LP = calculate_delirium(psychosis, alcohol_abuse, dementia, weight_loss, neurological_disorders, 
                      depression, fluid_elect_disorder, chf, drug_abuse, mi, coagulopathy, cerebro_vascular, renal_failure, pulmonary_circulation)
    
    # Classify the risk and get corresponding color
    risk_classification, color = classify_risk(LP)
    
    # Display result
    st.markdown(f"### Delirium Risk Index: {index}")
    st.markdown(f"### Risk Classification: {risk_classification}")
    
    # Display colored bar
    st.markdown(f"<div style='background-color:{color};height:20px;width:{min(LP, 5) / 5 * 100}%;'></div>", unsafe_allow_html=True)