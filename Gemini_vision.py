import google.generativeai as genai
import streamlit as st
from PIL import Image

def centered_content():
    col1, col2, col3 = st.columns([1, 12, 1])
    return col1, col2, col3

# Center-align the title
with centered_content()[1]:
    st.title(":blue[G]:red[o]:green[o]:blue[g]:green[l]:red[e] :blue[G]:red[e]:green[m]:blue[i]:green[n]:red[i] :blue[V]:red[i]:green[s]:blue[i]:green[o]:red[n]")

api_key = "AIzaSyB9i0slQTLC_5DZ29mbj1esnmtqdm1NfJg"
genai.configure(api_key=api_key)

uploaded_img = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_img is not None:
    st.image(Image.open(uploaded_img))
    prompt = st.text_input("Ask Something...")
    if st.button("Get Response"):
        img = Image.open(uploaded_img)
        model = genai.GenerativeModel("gemini-1.0-pro-vision-latest")
        with st.spinner("Thinking..."):
          response=model.generate_content([prompt,img])
          st.write(":green[Gemini Vision]:robot_face: :",response.text)
else:
    st.warning('Please Upload an Image..')
