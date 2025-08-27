from textblob import TextBlob
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_API_KEY")
if secret_key is None:
    raise ValueError("SECRET_API_KEY environment variable not set")

app = FastAPI()

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 3)  # -1 (negative) → 1 (positive)
    label = "POSITIVE" if polarity > 0 else "NEGATIVE" if polarity < 0 else "NEUTRAL"
    return {"label": label, "score": polarity}

@app.get("/sentiment")
def get_sentiment(text: str, api_key: str):
    if api_key == secret_key:
        return {"sentiment": analyze_sentiment(text)}
    else:
        return {"error": "Invalid API key"}