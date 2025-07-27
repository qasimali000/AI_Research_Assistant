import streamlit as st
import fitz
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain.llms import Ollama
from langchain_community.llms import Ollama
import os

# --- Setup ---
st.set_page_config(page_title="AI Research Assistant", layout="wide")

# Initialize Ollama with Mistral
llm = Ollama(model="mistral")  # Ensure you have `ollama pull mistral` done

# Setup embeddings and Chroma
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
persist_directory = "./data/vector_store"
vectorstore = Chroma(collection_name="documents", embedding_function=embedding_model, persist_directory=persist_directory)

# Memory for conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Create Conversational Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    memory=memory,
)

# --- Helper functions ---
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return ' '.join([p.get_text() for p in soup.find_all('p')])

def process_text_and_store(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    vectorstore.add_texts(chunks)
    vectorstore.persist()

# --- Streamlit UI ---
st.title("📚 Personal AI Research Assistant (Ollama + Mistral)")

tab1, tab2 = st.tabs(["Upload & Process Document", "Chat with Documents"])

with tab1:
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    url_input = st.text_input("Or enter a URL")

    if st.button("Process"):
        text = ""
        if uploaded_file:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            text = extract_text_from_pdf("temp.pdf")
        elif url_input:
            text = extract_text_from_url(url_input)

        if text:
            process_text_and_store(text)
            st.success("✅ Document processed and added to database.")

with tab2:
    st.subheader("💬 Chat with your documents")
    user_query = st.text_input("Ask a question")
    if user_query:
        with st.spinner("Thinking..."):
            response = qa_chain({"question": user_query})
        st.write("**Answer:**", response['answer'])

        # Debug output
        st.write("Raw Response:", response)

        if "source_documents" in response:
            with st.expander("View Sources"):
                for i, doc in enumerate(response['source_documents']):
                    st.markdown(f"**Source {i+1}:** {doc.page_content[:300]}...")

