# Delirium Risk Index (DRI) App

This repository contains an implementation of the Delirium Risk Index (DRI) model, designed to assess the likelihood of delirium in hospitalized patients based on their comorbidities. The DRI is calculated by summing the weighted contributions of key comorbidities, with weights derived from logistic regression coefficients, similar to methods used in previous comorbidity indices (e.g., Mukherjee et al).

The application is a practical tool for healthcare professionals to assess delirium risk, helping to support clinical decision-making in hospital settings.

## How It Works

The DRI model calculates a risk score based on patient-specific factors, including the presence of certain comorbidities. These comorbidities, identified as key risk factors for delirium, are assigned weights that reflect their relative importance in predicting the likelihood of delirium. The resulting DRI score classifies patients into low, medium, or high-risk categories.

### **Input:**  
Users manually input key patient data related to their medical history, selecting whether the patient has specific conditions like psychosis, alcohol abuse, dementia, or heart failure, among others.

### **Output:**  
The app processes the inputs and returns a DRI score along with a risk category:

- **Low Risk:** DRI score of 0–1
- **Medium Risk:** DRI score of 2–4
- **High Risk:** DRI score ≥ 5

The app also features a sliding bar visualization (green-to-red) to display the patient's risk score.

## Model Details

The DRI is based on a logistic regression model. The comorbidities included in the model were selected based on their significant contribution to predicting delirium risk. The coefficients from the logistic regression were multiplied by 5 and rounded to the nearest integer to assign each comorbidity a weight.

Key comorbidities included in the model are:
- Psychosis
- Alcohol abuse
- Dementia
- Weight loss
- Neurological disorders
- Depression
- Congestive heart failure
- And others...

## Summary

This application provides an easy-to-use, data-driven tool to estimate a patient's risk of delirium in a hospital setting. It can assist healthcare professionals in identifying high-risk patients early, allowing for timely interventions and more personalized care.
