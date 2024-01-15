import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
#from llama_index import PDFReader

st.title('🎈 huh?')

openai.api_key = st.secrets.openai_key
st.header("Chat with your uploaded file 💬 📚")

pdf_file = st.file_uploader('Choose your .pdf file', type="pdf")
