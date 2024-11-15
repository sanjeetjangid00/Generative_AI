import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API key for Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Function for centering content in Streamlit layout
def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

# Set up Streamlit layout
with centered_content()[1]:
    st.title(":green[Sentiment Analysis]")

# User input
chat = st.text_input("Ask Something...")

# Initialize Google Generative AI
genai.configure(api_key=api_key)

# Choose model (ensure "gemini-pro" is valid)
model = genai.GenerativeModel("gemini-pro")

# When the button is clicked
if st.button("Analyze Sentiment"):
    if chat:  # Check if the user has entered a query
        with st.spinner("Analyzing..."):
            # Request sentiment analysis from the model
            prompt = f"{chat} Tell me if this is only positive or negative."
            response = model.generate_content(prompt)
            
            # Display the results
            st.write(f"**User**: {chat}")
            st.write(f"**Gemini (Sentiment)**: {response.text}")
    else:
        st.warning("Please enter something to analyze.")
