
# 📚 Docling + Gemini RAG Pipeline

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline for answering questions from PDF and HTML documents.

---

## 🚀 Features
- Supports **PDF** and **HTML** document ingestion
- Document processing (HTML and PDF) using Docling.
- Stores embeddings in LanceDB
- Vector database creation and management with LanceDB.
- Embedding generation using the Gemini embedding model/(any other hugging face model).
- Retrieval of relevant document chunks based on user queries.
- Question answering using a language model (Gemini) with retrieved context.
- Interactive web interface using Streamlit.
- Works in **Google Colab** with Ngrok tunneling or locally
---

## 📂 Project Structure
```
files_for_docling
├── app.py               
├── databaselogic.py     
├── requirements.txt     
└── README.md            
````
- databaselogic.py: Contains the code for setting up the LanceDB database, processing documents (HTML and PDF) using Docling for chunking and conversion, and populating the database with document chunks and their embeddings.
- app.py: The Streamlit application that provides a user interface for asking questions about the documents stored in the LanceDB database. It retrieves relevant document chunks based on the user's query and uses a language model (Gemini) to generate answers based on the retrieved context.
- requirements.txt: Lists the Python dependencies required to run the project.
---

## 🛠 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Pritam11-web/docling-rag.git
cd files_for_docling
```


### 2️⃣ Install dependencies

```python
pip install -r requirements.txt
```


---

## 🔑 Setup

### 1. Required Environment Variables

You’ll need the following keys:

* `GOOGLE_API_KEY` → from [Google AI Studio](https://aistudio.google.com/app/apikey)
* `HF_TOKEN` → from [HuggingFace](https://huggingface.co/settings/tokens)
* `NGROK_AUTH_TOKEN` → from [Ngrok](https://dashboard.ngrok.com/get-started/your-authtoken) (only if running in Colab)

Create a `.env` file in `files_for_docling/`:

```env
GOOGLE_API_KEY=your_google_api_key
HF_TOKEN=your_huggingface_token
NGROK_AUTH_TOKEN=your_ngrok_token
```

---

### 2. Prepare Your Documents

In `databaselogic.py`, update the `document_urls` list:

```python
document_urls = [
    "https://example.com/document.pdf", #Your webpage url/document path
    "https://example.com/page.html"
]
```

Or use **local file paths** for PDFs.

---

## ▶️ Running the App

### **Option 1: Local Run**

```bash
streamlit run app.py
```

Then open the displayed local URL in your browser.

---

### **Option 2: Google Colab Run**

1. Upload all project files into your Colab working directory.
2. Install dependencies:
   ```python
   !pip install -r files_for_docling/requirements.txt

3. Install **pyngrok**:

   ```python
   !pip install pyngrok
   ```

4. Store secrets in Colab:

   * Go to **Colab** → **Tools** → **Secrets**.
   * Add the following:

     * `NGROK_AUTH_TOKEN` = *your ngrok token* (from [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken))
     * `GOOGLE_API_KEY` = *your Google API key*

5. Start ngrok tunnel and launch Streamlit:

   ```python
   from pyngrok import ngrok
   from google.colab import userdata
   import os, subprocess, time

   # Load secrets
   os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
   ngrok.set_auth_token(userdata.get("NGROK_AUTH_TOKEN"))

   # Kill old tunnels (if any)
   ngrok.kill()

   # Start tunnel
   public_url = ngrok.connect(addr="8501", proto="http")
   print(f"Streamlit app URL: {public_url}")

   # Run Streamlit
   process = subprocess.Popen(
       ['streamlit', 'run', 'files_for_docling/app.py', '--server.port', '8501'],
       env=os.environ
   )

   time.sleep(5)
   if process.poll() is None:
       print("✅ Streamlit is running...")
   else:
       print("❌ Failed to start Streamlit.")
   ```

6. Open the **public URL** printed above in your browser to access the app.

7. To build your LanceDB, run:

   ```python
   !python files_for_docling/databaselogic.py
   ```




---

## 💬 How to Use

1. **Start the app** (local or Colab).
2. Enter your question in the chat box.
3. The app:

   * Retrieves relevant chunks from LanceDB
   * Passes them with your question to Gemini
   * Displays an answer with source citations

---

## 📄 License

MIT License – free to use, modify, and distribute.

---

## 🙋‍♂️ Author

Made by **Pritam Saha**
📧 Email: [pritamsaha1109@gmail.com](mailto:pritamsaha1109@gmail.com)



