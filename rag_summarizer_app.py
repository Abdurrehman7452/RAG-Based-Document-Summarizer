import streamlit as st
from RAGSummarizer import RAGSummarizer  # Make sure the class is in RAGSummarizer.py or update the import path
import tempfile
import os

# Initialize the RAGSummarizer once
summarizer = RAGSummarizer()

st.set_page_config(page_title="RAG Document Summarizer", layout="wide")

st.title("📄 RAG Document Summarizer")
st.markdown("Upload a **PDF**, **TXT**, or **Markdown** file and get a smart summary using Retrieval-Augmented Generation (RAG).")

# File uploader
uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt", "md"])

# Query input
query = st.text_input("Enter your query (default: Summarize this document)", value="Summarize this document")

# Submit button
if uploaded_file and st.button("Generate Summary"):
    with st.spinner("Processing document..."):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        try:
            result = summarizer.process_document(tmp_path, query=query)
            
            # Display summary
            st.subheader("📝 Summary")
            st.success(result["summary"])

            # Expandable retrieved context
            with st.expander("📚 Retrieved Context"):
                for i, chunk in enumerate(result["retrieved_context"], 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.text(chunk)

            # Metadata
            st.markdown("### 📊 Metadata")
            st.json({
                "Similarity Scores": result["similarity_scores"],
                "Latency (s)": round(result["latency"], 2)
            })

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            os.remove(tmp_path)  # Clean up
