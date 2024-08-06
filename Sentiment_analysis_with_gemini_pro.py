import google.generativeai as genai
import streamlit as st

def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

with centered_content()[1]:
    st.title(":green[Sentiment Analysis]")
chat=st.text_input("Ask Something...")
api_key="AIzaSyDa7ZaRJJKcgHY0fPENj3eumUnl76Bpdis"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

if st.button("Response"):
    with st.spinner("Thinking..."):
        response=model.generate_content(chat+"tell me this is only positive or negative")
        st.write("User :adult: :", chat)
        st.write("Gemini :robot_face: :", response.text)
