import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import download_loader

st.title('🎈 huh?')

openai.api_key = st.secrets.openai_key
st.header("Chat with your uploaded file 💬 📚")

@st.cache_resource(show_spinner = False)
def load_data():
    with st.spinner(text = "Loading and indexing docs"):
        PDFReader = download_loader("PDFReader")
        reader = PDFReader(pdf_file)
        service_context = ServiceContext.from_defaults(llm = OpenAI(
                                                            model = "gpt-3.5-turbo",
                                                            temperature = .5,
                                                            system_prompt = 
                                                           "Your job is to answer questions on the relate to the documents. Keep your answers technical, based on facts, and explain your reasoning."))
        index = VectorStoreIndex.from_documents(reader, service_context = service_context)
        return index
        
pdf_file = st.file_uploader('Choose your .pdf file', type="pdf")


    if pdf_file not None:
        st.write("Uploaded Filename: ", file.name)

        # load data
        index = load_data()
    