from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
generator = pipeline("text-generation", model="csharp_gpt2")

@app.post("/chat")
async def chat(prompt: str):
    response = generator(prompt, max_length=100)
    return {"response": response[0]["generated_text"]}