# 📄 RAG Document Summarizer

This project is a **Retrieval-Augmented Generation (RAG)** based document summarizer built with Python, FAISS, HuggingFace Transformers, and Streamlit.

Upload a **PDF**, **TXT**, or **Markdown** file, and the system will retrieve the most relevant chunks and summarize them using a large language model.

---

## 🚀 Features

- 📚 Supports PDF, TXT, and MD formats.
- 🧠 Embeds content using `all-MiniLM-L6-v2`.
- ⚡ Uses FAISS for efficient semantic search.
- ✂️ Splits long documents into meaningful chunks.
- 🤖 Generates concise summaries using `facebook/bart-large-cnn`.
- 🌐 Simple, interactive UI built with Streamlit.

---

## 📸 Screenshots

#### 🔼 Upload a document
#### 📋 Summary Output
#### 📂 Retrieved Chunks
![doc1](https://github.com/user-attachments/assets/8c033ce4-993d-435f-afcc-ab6739ac15de)
![doc2](https://github.com/user-attachments/assets/a2a36dd7-5dfc-44f4-aa80-3407ecd16cff)




---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Run the app
```bash
streamlit run app.py
```

## 🧰 Tech Stack

Streamlit – UI

FAISS – Fast vector search

HuggingFace Transformers – LLM-based summarization

SentenceTransformers – Embedding model

Langchain – Text splitting utility

