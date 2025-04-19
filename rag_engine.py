from transformers import pipeline
import torch

GEN_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"
generator = pipeline("text-generation", model=GEN_MODEL, device=0 if torch.cuda.is_available() else -1)

def generate_response(query, top_matches):
    prompt = f"User query: {query}\n\nRecommended Assessments:\n"
    for item in top_matches:
        prompt += f"- {item['name']} ({item['duration']} min): {item['test_type']}\n"
    prompt += "\nGenerate a brief response explaining why these are recommended."

    result = generator(prompt, max_length=200, do_sample=True, temperature=0.7)
    return result[0]['generated_text'] if result else ""
