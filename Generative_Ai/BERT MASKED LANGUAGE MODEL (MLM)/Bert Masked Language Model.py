from transformers import pipeline
import streamlit as st

from transformers import BertTokenizer, BertModel
unmasker = pipeline('fill-mask',model="bert-base-uncased")
def centered_title():
  col1,col2,col3 = st.columns([1,12,1])
  return col1,col2,col3

with centered_title()[1]:
  st.title(":green[Bert Masked Language Model]")
st.write(":red[Note: Please write your sentence with [MASK] and Punctuation]")
st.write("For Example: How are [MASK]?")

text=st.text_input(label="Write your sentence with [MASK]")
if st.button(":green[Submit]"):
    if "[MASK]" in text:
      if text.strip():
        results=unmasker(text)
        st.success("Output Successfully Generated....")  
        for result in results:
          sequence=result['sequence']
          score=result['score']
          st.write(":red[Output-> ]", sequence)
          st.write(":blue[Score-> ]", score)
    else: 
      st.warning(":red[Please Write Your Sentence With [MASK] and Punctuation]")
else:
  st.warning("Please Write Your Sentence With [MASK] and Punctuation")
