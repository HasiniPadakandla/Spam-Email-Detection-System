import streamlit as st
import pickle

# Load trained model and vectorizer
model = pickle.load(open("spam_classifier_model.sav", "rb"))
vectorizer = pickle.load(open("feature_extraction_model.sav", "rb"))

# Page configuration
st.set_page_config(
    page_title="Spam Email Detection System",
    page_icon="📩",
    layout="centered"
)

# Title
st.title("📩 Spam Email Detection System")
st.write("Enter a message to check whether it is **Spam** or **Not Spam**.")

# User input
user_input = st.text_area("Message", height=150)

# Prediction
if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        input_features = vectorizer.transform([user_input])
        prediction = model.predict(input_features)[0]

        if prediction == 1:
            st.success("✅ This message is **NOT SPAM**")
        else:
            st.error("🚫 This message is **SPAM**")