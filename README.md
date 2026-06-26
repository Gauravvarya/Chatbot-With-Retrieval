# 📄 Document Retrieval Chatbot using Gemini + FAISS

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from PDF documents using Google's Gemini AI, LangChain, and FAISS Vector Store.

---

## 🚀 Features

- 📑 Upload and process PDF documents
- 🔍 Semantic search using FAISS
- 🤖 Google Gemini for answer generation
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Context-aware responses
- 🔒 API key stored securely using `.env`

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- LangChain
- FAISS
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
document-retrieval-chatbot/
│── data/
│   └── documents.pdf
│── faiss_store/
│── app.py
│── ingest.py
│── requirements.txt
│── .env.example
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Gauravvarya/Chatbot-With-Retrieval.git
```

Go to project directory

```bash
cd Chatbot-With-Retrieval
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 📥 Create Vector Store

```bash
python ingest.py
```

---

## ▶️ Run Chatbot

```bash
python app.py
```

---

## 💬 Example Questions

- What is System Design?
- Explain CAP Theorem.
- What is Scalability?
- Difference between Latency and Throughput?
- What are Consistency Patterns?

---

## 📌 Future Improvements

- Streamlit Web UI
- Multiple PDF Support
- Chat History
- Source Citations
- PDF Upload Interface

---

## 👨‍💻 Author

**Gaurav Kumar Singh**

GitHub: https://github.com/Gauravvarya

---

⭐ If you like this project, consider giving it a Star.
