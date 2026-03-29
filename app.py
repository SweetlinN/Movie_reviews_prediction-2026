import streamlit as st
import joblib

# Load model
model = joblib.load('model.joblib')

# Optional: load vectorizer if you used one
# vectorizer = joblib.load('vectorizer.joblib')

# App title
st.title("📝 Movie Reviews Prediction")

# User input
user_input = st.text_area("Enter your review:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # If you used vectorizer, uncomment below:
            # transformed = vectorizer.transform([user_input])
            # prediction = model.predict(transformed)

            prediction = model.predict([user_input])

            st.success(f"Prediction: {prediction[0]}")

        except Exception as e:
            st.error(f"Error: {e}")
