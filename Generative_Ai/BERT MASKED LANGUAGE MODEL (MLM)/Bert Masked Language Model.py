from transformers import pipeline
import streamlit as st

from transformers import BertTokenizer, BertModel
unmasker = pipeline('fill-mask',model="bert-base-uncased")
def centered_title():
  col1,col2,col3 = st.columns([1,7,1])
  return col1,col2,col3

with centered_title()[1]:
  st.title(":green[Bert Mask Language Model]")
st.write(":red[Note: Please write your sentence with [MASK]]")
st.write("For Example: How are [MASK]?")

text=st.text_input(label="Write your sentence with [MASK]")
if st.button(":green[Submit]"):
    if text.strip():
      results=unmasker(text)  
      for result in results:
        sequence=result['sequence']
        score=result['score']
        st.write(":red[Output-> ]", sequence)
        st.write(":blue[Score-> ]", score)
    else: 
      st.warning(":red[Please Write Your Sentence With [MASK]]")
else:
  st.warning("Please Write Your Sentence With [MASK]")
