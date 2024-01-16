import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from pypdf import PdfReader

st.title('🎈 huh?')

openai.api_key = st.secrets.openai_key
st.header("Chat with your uploaded file 💬 📚")

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

#@st.cache_resource(show_spinner = False)
def load_data(text):
    with st.spinner(text = "Loading and indexing docs"):
        documents = Document(text = text)
        service_context = ServiceContext.from_defaults(llm = OpenAI(
                                                            model = "gpt-3.5-turbo",
                                                            temperature = .5,
                                                            system_prompt = 
                                                           "Your job is to answer questions on the relate to the documents. Keep your answers technical, based on facts, and explain your reasoning."))
        index = VectorStoreIndex.from_documents(documents, service_context =                         service_context)
        return index


pdf_file = st.file_uploader('Choose your .pdf file', type="pdf")

if pdf_file is not None:
    st.write("Uploaded Filename: ", pdf_file.name)
    
    text = get_pdf_text(pdf_file)
    st.write("PDF content extracted...previewing first 100 characters")
    st.write(text[:100])
    
    # load data
    if st.button('Load data: '):
        index = load_data()
    
    st.header('Ask your data')

    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
    
    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])
        
    # if last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Tinkin..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message history 

   
