import google.generativeai as genai
import streamlit as st
import time
def centered_content():
    col1, col2, col3 = st.columns([1, 3, 1])
    return col1, col2, col3

# Center-align the title
with centered_content()[1]:
    st.title(":blue[G]:red[e]:green[m]:blue[i]:green[n]:red[i] :blue[P]:red[o]:green[w]:blue[e]:green[r]:red[e] :blue[d]:red[C]:green[h]:blue[a]:green[t]:red[b]:blue[o]:green[t]")
    
chat=st.chat_input("Ask Something...",key=2003,disabled=False)
api_key="AIzaSyB9i0slQTLC_5DZ29mbj1esnmtqdm1NfJg"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

def chatting(chat):
    return model.generate_content(chat)
def stream_data(response):
            st.write(":green[Gemini] :robot_face: :")
            for word in response.text.split(" "):
                yield word + " "
                time.sleep(0.02)
if chat:
    st.write(":blue[User] :adult: :", chat)
    with st.spinner("Generating...."):
        #st.write(":green[Gemini] :robot_face: :")
        response = chatting(chat)
        st.write_stream(stream_data(response))

else:
    st.warning("Please type something to generate content.")
    st.write(":blue[Gemini] :robot_face: : :green[Hi ! How can I assist you today?]")
