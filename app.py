import streamlit as st
import joblib

# Load model
import os
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.joblib")

model = joblib.load(model_path)
model.fit(reviews_train, sent_train)
vectorizer = joblib.load('vectorizer.joblib')

transformed = vectorizer.transform([user_input])
prediction = model.predict(transformed)

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
            model = joblib.load("model.joblib")
        except Exception as e:
             st.error(f"Model loading failed: {e}")
