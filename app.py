import streamlit as st
from backend import run_pipeline  # your main.py logic

st.title("📄 Agentic RAG Chatbot")
uploaded_files = st.file_uploader("Upload documents", accept_multiple_files=True)
question = st.text_input("Ask your question:")

if st.button("Submit"):
    with st.spinner("Processing..."):
        result = run_pipeline(uploaded_files, question)
        st.write("### Answer:", result["answer"])
        st.write("#### Context:", result["context"])
