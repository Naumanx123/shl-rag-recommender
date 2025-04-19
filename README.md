# SHL Assessment Recommender (RAG-Based)

This project uses RAG with FAISS + Mistral to recommend SHL assessments based on natural language queries.

## How to Run
```bash
# 1. Backend
cd app
uvicorn main:app --reload

# 2. Frontend
streamlit run streamlit_app/ui.py
```

## Deployment
- Deploy on Hugging Face Spaces (Docker)
