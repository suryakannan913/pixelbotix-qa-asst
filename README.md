# Pixelbotix QA Assistant

A Retrieval-Augmented Generation (RAG) based, context-aware Question Answering assistant built in Python. The project uses modern LLM tooling (Google Gemini via `google-genai`) and a vector store to ingest documents and answer questions based on their content.

---

## 🚀 Features

* Context-aware QA using RAG
* Document ingestion (PDF/text)
* Embeddings + vector store for retrieval
* Google Gemini (GenAI) as the LLM backend
* Cross-platform support (macOS, Windows, Linux)

---

## 📦 Prerequisites

Before you begin, make sure you have:

* **Python 3.10+** (3.11 recommended)
* **Git** installed
* A **Google Gemini API key**

Check your Python version:

```bash
python --version
```

---

## 🔑 API Key Setup (Required)

This project uses **Google Gemini** via the `google-genai` SDK.

### 1. Create an API key

* Go to **Google AI Studio**: [https://aistudio.google.com/](https://aistudio.google.com/)
* Navigate to **API Keys**
* Create a new API key

### 2. Create a `.env` file

In the project root, create a file named `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
```

⚠️ **Do not commit `.env` to GitHub**. It is already ignored via `.gitignore`.

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-org-or-username>/pixelbotix-qa-asst.git
cd pixelbotix-qa-asst
```

### 2. Create a virtual environment

```bash
python -m venv my_venv
```

Activate it:

**macOS / Linux**

```bash
source my_venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.\my_venv\Scripts\activate
```

### 3. Install dependencies

All required dependencies are listed in `requirements.txt`.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Make sure your virtual environment is activated and `.env` is configured.

```bash
python app.py
```

If the setup is correct, the application will start without authentication or import errors.

---

## 🔒 Security Best Practices

* Never hard-code API keys
* Always use environment variables
* Rotate keys immediately if exposed
* Use `.env.example` to document required variables

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

MIT License (or update as appropriate)

---

## 📬 Support

If you run into issues:

* Double-check Python version and virtual environment
* Ensure `requirements.txt` dependencies are installed
* Verify `GOOGLE_API_KEY` is set

Happy building 🚀
