import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

st.title('🎈 huh?')

openai.api_key = st.secrets.openai_key
st.header("Chat with your uploaded file 💬 📚")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question!"}
    ]
    
@st.cache_resource(show_spinner = False)

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file:
    st.write("FIlename: ", uploaded_file.name)
