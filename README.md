
# 🧠 AI Research Assistant (Local LLM with Ollama + LangChain + Streamlit)

A privacy-focused, offline-friendly AI assistant that lets you:
- 📄 Upload and process PDFs or paste web URLs
- 🔍 Chat with documents using semantic search (RAG)
- 💬 Get contextual answers powered by a local LLM (Mistral 7B via Ollama)
- 💾 Store documents in a persistent vector database (ChromaDB)

No API keys. No external dependencies. 100% local.

---

## 🚀 Features

- ✅ Upload PDFs or paste article URLs
- ✅ Extract and chunk document text
- ✅ Embed using `sentence-transformers`
- ✅ Store in persistent **ChromaDB**
- ✅ Ask questions using **LangChain RAG pipeline**
- ✅ Local LLM via **Ollama + Mistral**
- ✅ Streamlit-based web UI

---

## 🛠️ Tech Stack

| Layer        | Tool                      |
|--------------|---------------------------|
| UI           | Streamlit                 |
| LLM          | Mistral (via Ollama)      |
| RAG Logic    | LangChain                 |
| Embeddings   | SentenceTransformers      |
| Vector Store | ChromaDB                  |
| Parsing      | PyMuPDF, BeautifulSoup    |

---

## 📦 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama & Pull Mistral

**macOS/Linux:**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Or via Homebrew (macOS)
brew install ollama/tap/ollama

# Pull Mistral model
ollama pull mistral
```

**Check it works:**
```bash
ollama run mistral "What is LangChain?"
```

---

## 💻 Run the App

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser.

---

## 🧠 How It Works

1. Upload a PDF or paste a URL.
2. Text is extracted, chunked, and embedded using `all-MiniLM-L6-v2`.
3. Embeddings are stored in **ChromaDB**.
4. You can chat with the document using **LangChain**’s RAG pipeline.
5. Questions are answered using **Mistral 7B**, running locally via **Ollama**.

---

## 📁 Project Structure

```
ai-research-assistant/
│
├── app.py               # Streamlit app
├── requirements.txt     # Python dependencies
└── data/
    └── vector_store/    # ChromaDB persistent store
```

---

## 🔒 Privacy First

This project:
- Runs entirely locally
- Stores data only on your machine
- Does not require internet for LLM inference

---

## 🧩 To-Do / Upcoming Features

- [ ] Streaming chat responses
- [ ] Document management UI (list/delete)
- [ ] Highlight relevant passages
- [ ] Multi-user support
- [ ] Docker deployment

---

## 📜 License

MIT License. See `LICENSE`.

---

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.ai)
- [Mistral](https://mistral.ai)
- [ChromaDB](https://www.trychroma.com/)
- [Hugging Face Sentence Transformers](https://www.sbert.net/)

---

## ✨ Screenshots

| Upload & Process | Chat with Document |
|------------------|-------------------|
| ![upload](./assets/upload.png) | ![chat](./assets/chat.png) |

---

## 🤝 Contribute

Pull requests are welcome! Feel free to open issues for suggestions or bugs.

---
