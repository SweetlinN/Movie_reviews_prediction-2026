import streamlit as st
import joblib

# Load model
model = joblib.load('model.joblib')

st.title("Review Sentiment Predictor")

user_input = st.text_area("Enter a review:")

if st.button("Predict"):
    if user_input.strip():
        prediction = model.predict([user_input])
        st.write("Prediction:", prediction[0])
    else:
        st.write("Please enter some text.")
