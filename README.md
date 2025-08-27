# 🚀 Sentiment Analysis API

A production-ready REST API that uses Hugging Face’s **DistilBERT** model (fine-tuned on SST-2) to perform sentiment analysis (positive/negative) on text.  
Built with **FastAPI**, deployed on **Render**, and secured with an API key.

---

## 🌐 Live Demo
- **Swagger UI**: [https://your-render-url.onrender.com/docs](https://your-render-url.onrender.com/docs)  
- **Endpoint**:  
  ```
  https://your-render-url.onrender.com/sentiment?text=I%20love%20this!&api_key=YOUR_SECRET_API_KEY
  ```

Example request (with `curl`):
```bash
curl "https://your-render-url.onrender.com/sentiment?text=I%20love%20this!&api_key=YOUR_SECRET_API_KEY"
```

Example response:
```json
{
  "sentiment": {
    "label": "POSITIVE",
    "score": 0.9987
  }
}
```

---

## ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ChrisCaston/ml-project-sentiment-analysis.git
   cd ml-project-sentiment-analysis
   ```

2. **Create and activate a virtual environment:**
   * macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   * Windows:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Configuration

The API requires a secret key for authentication.

1. Create a `.env` file in the root of your project:
   ```
   SECRET_API_KEY=mysupersecret123
   ```

2. Or set it directly in your shell:
   ```bash
   export SECRET_API_KEY=mysupersecret123
   ```

---

## ▶️ Running the API Locally

Start the API using Uvicorn:
```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

Then visit:
- [http://localhost:10000/docs](http://localhost:10000/docs) → Swagger UI  
- Or call directly:
  ```
  http://localhost:10000/sentiment?text=Your_text_here&api_key=Your_api_key_here
  ```

---

## 🛠 Tech Stack
- **Python**
- **FastAPI** for REST API
- **Hugging Face Transformers** (DistilBERT sentiment model)
- **PyTorch** as the deep learning backend
- **Render** for deployment

---

## 📊 About the Sentiment Score
- Returns a **label** (`POSITIVE` or `NEGATIVE`)  
- Returns a **confidence score** (0 → 1) using softmax probabilities  

---

## 📄 License
MIT