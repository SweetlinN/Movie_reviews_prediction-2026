import streamlit as st
import joblib

# Load model
model = joblib.load("Movie_reviews.pkl")

# Title
st.title("🎬 Movie Review Sentiment Analysis")

# Input box
review = st.text_area("Enter your movie review:")

# Predict button
if st.button("Predict"):
    if review.strip() != "":
        prediction = model.predict([review])
        
        if prediction[0] == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")
    else:
        st.warning("Please enter a review")
