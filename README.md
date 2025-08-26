# Simple Sentiment Analysis API

A lightweight REST API that uses a Hugging Face model to perform sentiment analysis on a given text.

### Setup and Installation

1.  **Clone the repository:**
    
    ```
    git clone [https://github.com/ChrisCaston/ml-project-sentiment-analysis.git](https://github.com/ChrisCaston/ml-project-sentiment-analysis.git)
    ```

2.  **Create and activate a virtual environment:**
    
    * For macOS/Linux:
        ```
        python3 -m venv env
        source env/bin/activate
        ```
    * For Windows:
        ```
        python3 -m venv env
        .\env\Scripts\activate
        ```

3.  **Install dependencies:**
    
    ```
    pip install -r requirements.txt
    ```

---

### Configuration

The API requires a secret key for authentication. You will need to set up a `.env` file to store your key.

1.  Create a file named `.env` in the root of your project.
2.  Add your own secret key to the file. For example:

    ```
    SECRET_API_KEY="mysecretapikey123"
    ```

---

### Running the API

Once configured, you can start the API using Uvicorn.

uvicorn app:app --reload --port 8000


---

### Calling the API

Once the server is running, you can call the API by visiting a URL in your browser or using a tool like `curl`.

**URL:** `http://127.0.0.1:8000/sentiment?text=Your_text_here&api_key=your_api_key`

* Replace `Your_text_here` with the text you want to analyze.
* Replace `your_api_key` with the secret key you set in your `.env` file.