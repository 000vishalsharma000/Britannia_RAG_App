import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import io
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
os.environ["HUGGINGFACE_TOKEN"] == st.secrets["HUGGINGFACE_TOKEN"]

# Hugging Face API endpoint and headers
# API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer "+ str(os.getenv('HUGGINGFACE_TOKEN'))}

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to query Hugging Face API
def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Function to generate response using Hugging Face and Chroma
def generate_response(uploaded_file, query_text):
    if uploaded_file is not None:
        document_text = extract_text_from_pdf(uploaded_file)
        documents = [document_text]
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.create_documents(documents)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = Chroma.from_documents(texts, embeddings)
        retriever = db.as_retriever()

        # Retrieve relevant documents
        relevant_docs = retriever.get_relevant_documents(query_text)

        # # Limit to the top 1 or 2 most relevant documents
        # max_docs = 1
        # relevant_docs = relevant_docs[:max_docs]

        combined_input = f"User Query: {query_text}\n\nRelevant Information:\n"
        for doc in relevant_docs:
            combined_input += f"{doc}\n"
        combined_input += "\nPlease generate a detailed answer based on the above information."

        # print(len(combined_input))

        # Generate response using Hugging Face API
        response = query_huggingface({"inputs": combined_input})

        # Extract generated_text from the response
        generated_text = response[0]['generated_text'] if response and response[0].get('generated_text') else ""

        # Find index where the answer starts
        start_index = generated_text.find("Answer:")
        ans=generated_text[start_index:]
        
        return ans

# Set page configuration and customizations
st.set_page_config(
    page_title='Britannia RAG App',
    page_icon=':british_flag:', 
    layout='wide',
    initial_sidebar_state='expanded',
)

# Custom CSS for background color and text color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display Britannia logo at the top
britannia_logo_url = 'https://zeevector.com/wp-content/uploads/Britannia-Logo-PNG@ZEEVECTOR.png'
st.image(britannia_logo_url, use_column_width=True)

# Main application layout
st.title('Britannia RAG App')

st.sidebar.header('Upload Document')
uploaded_file = st.sidebar.file_uploader('Upload an article', type='pdf')

query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.', disabled=not uploaded_file)

result = []
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted:
        with st.spinner('Calculating...'):
            response = generate_response(uploaded_file, query_text)
            result.append(response)

if len(result):
    st.info(result[0])

# st.sidebar.subheader("Get an OpenAI API key")
# st.sidebar.write("You can get your own OpenAI API key by following the instructions:")
# st.sidebar.write("""
# 1. Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys).
# 2. Click on the `+ Create new secret key` button.
# 3. Next, enter an identifier name (optional) and click on the `Create secret key` button.
# """)
