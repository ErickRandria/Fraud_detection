import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_model.pkl')
st.title("Fraud Detection App")
st.write("This app predicts whether a transaction is fraudulent or not.")
st.markdown("Please enter the transaction details and use the button below to predict.")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASHOUT", "DEPOSIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value = 1000.0)
old_balance = st.number_input("Old Balance", min_value=0.0, value = 10000.0)
new_balance = st.number_input("New Balance", min_value=0.0, value = 9000.0)
old_balance_dest = st.number_input("Old Balance Destination", min_value=0.0, value = 0.0)
new_balance_dest = st.number_input("New Balance Destination", min_value=0.0, value = 0.0)

if st.button("Predict"):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [old_balance],
        'newbalanceOrig': [new_balance],
        'oldbalanceDest': [old_balance_dest],
        'newbalanceDest': [new_balance_dest]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction : '{int(prediction)}'")

    # Display the reslsult
    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")

    # st.write(f"Prediction Probability: {prediction_proba[0][1]:.2f}")