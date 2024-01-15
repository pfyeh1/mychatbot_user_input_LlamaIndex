import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader


st.title('🎈 App Name')

st.write('Hello world!')

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file:
    st.write("FIlename: ", uploaded_file.name)
