from fastapi import FastAPI, Request
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

load_dotenv()
app = FastAPI()
try:
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
    question_gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    print("Model loaded successfully.")

except Exception as e:
    print(f"Error loading model: {e}")
    question_gen = None

# allow cors for Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "chrome-extension://*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str
    
# generate questions via Gemini given str content of page
def generateQuestions(text: str):
    text = text[0:2048]  # limit to 2048 characters

    if not text:
        return {"error": "No content provided."}
    
    if question_gen is None:
        return {"error": "Model not loaded."}

    prompt = "generate Multiple Choice Questions based on the following content: " + text
    outputs = question_gen(prompt, max_length=512, num_return_sequences=5, num_beams=5, do_sample=True, top_k=50, top_p=0.95)

    flashcards = []
    for output in outputs:
        question = output['generated_text']
        if question:
            flashcards.append({"question": question}) 
            
    return {"flashcards": flashcards}

@app.get("/")
def read_root():
    return "Hello, World... Access Page Here: "

@app.post("/api/generate")
def generate(body: dict):
    content = body.get("content", "")
    token = body.get("token", "")
    return generateQuestions(content)
