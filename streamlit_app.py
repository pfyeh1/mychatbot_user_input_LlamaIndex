import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from pypdf import PdfReader

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
                                                           "Your job is to answer questions on the relate to the documents. Keep your                                                                     answers technical, based on facts, and explain your reasoning."))
        index = VectorStoreIndex.from_documents(reader, service_context = service_context)
        return index
        
        
def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def process_text(text):
    doc = Document(text = text)
    return [doc]


pdf_file = st.file_uploader('Choose your .pdf file', type="pdf")

if pdf_file is not None:
    st.write("Uploaded Filename: ", pdf_file.name)
    
    text = get_pdf_text(pdf_file)
    st.write("PDF content extracted!")
    st.write(text)
    

   
