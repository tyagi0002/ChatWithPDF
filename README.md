
# 📚 ChatWithPDF

**ChatWithPDF** is an intelligent PDF chat assistant powered by LangChain, Hugging Face embeddings, Google Gemini (PaLM), and ChromaDB. It enables you to load, process, embed, and query PDF documents using natural language.

---

## 🚀 Features

- 📥 Load any PDF file
- 🧠 Split and vectorize document using embeddings
- 🔎 Retrieve relevant document chunks using similarity search
- 💬 Ask questions and get accurate, LLM-generated answers
- 🤖 Powered by Google's Gemini 2.0 Flash and Hugging Face

---

## 🧱 Tech Stack

- **LangChain** – Framework for chaining LLMs and tools
- **ChromaDB** – Lightweight vector store for fast retrieval
- **Hugging Face Embeddings** – `all-MiniLM-L6-v2` for semantic search
- **Google Gemini 2.0 Flash** – LLM for generating answers
- **RecursiveCharacterTextSplitter** – Efficient chunking of text
- **Python Dotenv** – For managing API keys securely

---

## 📁 Project Structure

```
.
├── main.py               # Core script to process and query PDF
├── requirements.txt      # Dependencies list
```

---

## 🔧 Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt

pip install langchain-community pypdf

```

### 2. 🔐 Configure Environment

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> Replace `your_google_gemini_api_key` with your actual API key.

### 3. 📄 Add Your PDF File

Place your PDF in the project directory and update this line in `main.py`:

```python
loader = PyPDFLoader('YOUR_PDF_FILE.pdf')
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

It will:

1. Load and parse your PDF
2. Split it into chunks
3. Generate embeddings and store them in Chroma
4. Use similarity search to retrieve top 5 chunks
5. Ask the LLM your query
6. Print the structured answer

---

## 🧪 Example Prompt (Inside Code)

```python
query = "Give the Cloud project and related details."
```

---

## 📌 Notes

- This version uses a hardcoded query. You can easily modify it to take `input()` from users.
- Make sure the PDF file isn't scanned (non-text PDFs will not parse properly).

---

## 📜 License

MIT License – Free to use and modify.

---

## 🤝 Contributions

Pull requests and suggestions are welcome to improve:
- Interactive chat interface (e.g., using Streamlit)
- Caching or multi-file support
- PDF OCR fallback
