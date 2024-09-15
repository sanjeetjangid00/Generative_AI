import google.generativeai as genai
import streamlit as st
import time
def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

# Center-align the title
with centered_content()[1]:
    st.title(":blue[G]:red[o]:green[o]:blue[g]:green[l]:red[e] :blue[G]:red[e]:green[m]:blue[i]:green[n]:red[i] :blue[P]:red[r]:green[o]")
    
chat=st.chat_input("Ask Something...",key=2003,disabled=False)
api_key="AIzaSyB9i0slQTLC_5DZ29mbj1esnmtqdm1NfJg"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

def chatting(chat):
    return model.generate_content(chat)
def stream(response):
            st.write(":green[Gemini] :robot_face: :")
            for word in response.text.split(" "):
                yield word + " "
                time.sleep(0.02)
if chat:
    st.write(":blue[User] :adult: :", chat)
    with st.spinner("Generating...."):
        #st.write(":green[Gemini] :robot_face: :")
        response = chatting(chat)
        st.write_stream(stream(response))

else:
    st.warning("Please type something to generate content.")
    st.write(":blue[Gemini] :robot_face: : :green[Hi ! How can I assist you today?]")
    st.write_stream()
