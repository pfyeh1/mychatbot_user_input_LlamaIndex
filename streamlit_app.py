import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import PDFReader

st.title('🎈 huh?')

openai.api_key = st.secrets.openai_key
st.header("Chat with your uploaded file 💬 📚")


@st.cache_resource(show_spinner = False)
pdf_file = st.file_uploader('Choose your .pdf file', type="pdf")

@st.cache_resource(show_spinner = False)
def load_data():
    with st.spinner(text = "Loading and indexing docs"):
        reader = PDFReader(pdf_file)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm = OpenAI(
                                                            model = "gpt-3.5-turbo",
                                                            temperature = .5,
                                                            system_prompt = 
                                                           "Your job is to answer questions on the relate to the documents. Keep your answers technical, based on facts, and explain your reasoning."))
        index = VectorStoreIndex.from_documents(docs, service_context = service_context)
        return index
        
if pdf_file not None:
    st.write("Filename: ", pdf_file.name)
    
    if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question!"}
    ]
    
    # load data
    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])
        
        
    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Tinkin..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message history