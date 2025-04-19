from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.model import load_data_and_index, get_recommendations
from app.rag_engine import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products, model, index = load_data_and_index()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommend")
def recommend(query: str = Query(..., description="User query or job description")):
    top_matches = get_recommendations(query, model, index, products)
    response = generate_response(query, top_matches)
    return {"query": query, "results": top_matches, "response": response}
