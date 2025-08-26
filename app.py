import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from fastapi import FastAPI
import uvicorn
import os

secret_key = os.getenv("SECRET_API_KEY")

if secret_key is None:
    raise ValueError("SECRET_API_KEY environment variable not set")

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

app = FastAPI()

def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]

@app.get("/sentiment")
def get_sentiment(text: str, api_key: str):
    if api_key == secret_key:
        return {"sentiment": analyze_sentiment(text)}
    else:
        return {"error": "Invalid API key"}