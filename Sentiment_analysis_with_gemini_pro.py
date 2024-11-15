import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

with centered_content()[1]:
    st.title(":green[Sentiment Analysis]")
chat=st.text_input("Ask Something...")



genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel("gemini-pro")

if st.button("Response"):
    with st.spinner("Thinking..."):
        response=model.generate_content(chat+"tell me this is only positive or negative")
        st.write("User :adult: :", chat)
        st.write("Gemini :robot_face: :", response.text)
