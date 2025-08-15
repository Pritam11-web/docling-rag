
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
├── app.py               # Streamlit app (frontend + retrieval logic)
├── databaselogic.py     # Database creation + document processing
├── requirements.txt     # Dependencies list
└── README.md            # This file
````
- databaselogic.py: Contains the code for setting up the LanceDB database, processing documents (HTML and PDF) using Docling for chunking and conversion, and populating the database with document chunks and their embeddings.
- app.py: The Streamlit application that provides a user interface for asking questions about the documents stored in the LanceDB database. It retrieves relevant document chunks based on the user's query and uses a language model (Gemini) to generate answers based on the retrieved context.
- requirements.txt: Lists the Python dependencies required to run the project.
---

## 🛠 Installation

### 1️⃣ Clone the repository

git clone https://github.com/Pritam11-web/docling-rag.git
cd files_for_docling


### 2️⃣ Install dependencies


pip install -r requirements.txt


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
   ```
3. Set Colab secrets for:

   * `GOOGLE_API_KEY`
   * `HF_TOKEN`
   * `NGROK_AUTH_TOKEN`
4. Run `databaselogic.py` to build your LanceDB.
5. Run `app.py` via Ngrok tunnel:

   ```python
   public_url = ngrok.connect(addr="8501", proto="http")
   !streamlit run files_for_docling/app.py --server.port 8501
   ```
6. Open the `public_url` in your browser.

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

```


