import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(__file__)

encoder_files = {
    "Sex": "Sex_encoder.pkl",
    "Housing": "Housing_encoder.pkl",
    "Saving_accounts": "Saving accounts_encoder.pkl",
    "Checking_account": "Checking account_encoder.pkl"
}

model = joblib.load('extra_trees_credit_model.pkl')
encoder = {
    col: joblib.load(os.path.join(BASE_DIR, fname))
    for col, fname in encoder_files.items()
}


st.title("Credit Risk Prediction App")
st.write("Enter the details below to predict credit risk is good or bad.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ['little', 'moderate', 'quite rich', 'rich'])
checking_account = st.selectbox("Checking account", ['moderate', 'little', 'rich'])
credits_amount = st.number_input("Credit amount", min_value=100, max_value=100000, value=5000)
duration = st.number_input("Duration (months)", min_value=1, max_value=60, value=12)


input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [encoder['Sex'].transform([sex])[0]],
    'Job': [job],
    'Housing': [encoder['Housing'].transform([housing])[0]],
    'Saving accounts': [encoder['Saving_accounts'].transform([saving_accounts])[0]],
    'Checking account': [encoder['Checking_account'].transform([checking_account])[0]],
    'Credit amount': [credits_amount],
    'Duration': [duration]
})


if st.button("Predict Credit Risk"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("The credit risk is GOOD.")
    else:
        st.error("The credit risk is BAD.")