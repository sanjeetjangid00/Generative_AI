import google.generativeai as genai
import streamlit as st

def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

# Center-align the title
with centered_content()[1]:
    st.title(":blue[G]:red[o]:green[o]:blue[g]:green[l]:red[e] :blue[G]:red[e]:green[m]:blue[i]:green[n]:red[i] :blue[P]:red[r]:green[o]")
chat=st.chat_input("Ask Something...",key=2003,disabled=False)
api_key="AIzaSyC_L3-d181ibSultwSEuGm6P4XwE8HIsEQ"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")
if chat:
    response=model.generate_content(chat)
    st.write("User :adult: :", chat)
    st.write("Gemini :robot_face: :", response.text)
    #st.sidebar.text_area("Human :adult:", value=chat, height=100, max_chars=None)
    #st.sidebar.text_area("ChatGpt :robot_face:", value=response.text, height=200, max_chars=None)
else:
    st.warning("Please type something to generate content.")
    def centered_content():
        col1, col2, col3 = st.columns([4, 1, 4])
        return col1, col2, col3
    with centered_content()[1]:
        st.title(":blue[Hi!]")