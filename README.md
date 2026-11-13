# Proyek ChatBot & LangServe API (LangChain)

Proyek ini berisi implementasi chatbot berbasis **LangChain**, menggunakan model lokal (**Ollama Llama 3.2**) dan cloud (**Google Gemini**), serta penyediaan backend API menggunakan **FastAPI & LangServe** dengan antarmuka **Streamlit**.

---

## 📁 Struktur Direktori

```text
Buat ChatBot/
├── api/
│   ├── app.py          # FastAPI backend server dengan rute LangServe (/essay & /poem)
│   ├── client.py       # Streamlit client untuk berinteraksi dengan LangServe API
│   └── cline.py        # Salinan client streamlit
├── chatbot/
│   ├── app.py          # Antarmuka chatbot Streamlit langsung dengan Google Gemini
│   ├── localama.py     # Antarmuka chatbot Streamlit langsung dengan Ollama (Llama 3.2)
│   └── requirements.txt
├── .env                # File konfigurasi API Key (Google, LangChain)
├── requirements.txt    # Daftar dependensi lengkap proyek
└── README.md           # Petunjuk penggunaan proyek
```

---

## 🛠️ Prasyarat Sistem

1. **Python 3.10+** (sudah diuji pada Python 3.14).
2. **Ollama**:
   - Pastikan Ollama telah terinstal dan berjalan di sistem Anda.
   - Unduh model `llama3.2` melalui terminal jika belum:
     ```bash
     ollama pull llama3.2
     ```
3. **Google Gemini API Key**:
   - Dapatkan API key dari [Google AI Studio](https://aistudio.google.com/).
4. **LangChain API Key** _(opsional)_:
   - Untuk pelacakan prompt & evaluasi via LangSmith.

---

## ⚙️ Instalasi & Konfigurasi

### 1. Instal Dependensi

Jalankan perintah berikut di terminal:

```powershell
py -m pip install -r requirements.txt
```

### 2. Atur Environment Variables (`.env`)

Buat atau sesuaikan file `.env` di folder root proyek dengan isi:

```env
GOOGLE_API_KEY=your_google_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

---

## 🚀 Cara Menjalankan Aplikasi

### Opsi 1: Chatbot Lokal Ollama (Streamlit Langsung)

Menjalankan chatbot interaktif menggunakan model lokal Ollama (Llama 3.2):

```powershell
py -m streamlit run chatbot\localama.py
```

> Buka browser di `http://localhost:8501`.

---

### Opsi 2: Chatbot Google Gemini (Streamlit Langsung)

Menjalankan chatbot menggunakan model Google Gemini:

```powershell
py -m streamlit run chatbot\app.py
```

> Buka browser di `http://localhost:8501`.

---

### Opsi 3: Menjalankan API Server LangServe (FastAPI Backend)

Backend ini menyajikan rute Runnable LangChain:

- `/gemini` : Pembuatan essay menggunakan Google Gemini
- `/ollama` : Pembuatan puisi menggunakan Ollama Llama 3.2

Jalankan server API:

```powershell
py api\app.py
```

- Server API aktif di: `http://localhost:8000`
- Swagger UI / Dokumentasi API: `http://localhost:8000/docs`
- LangServe Playground Ollama: `http://localhost:8000/poem/playground/`
- LangServe Playground Gemini: `http://localhost:8000/essay/playground/`

---

### Opsi 4: Menjalankan Client Streamlit untuk LangServe

Saat server API (`py api\app.py`) sedang aktif, buka terminal baru lalu jalankan client:

```powershell
py -m streamlit run api\client.py
```

Aplikasi client akan terhubung ke backend FastAPI di port `8000`.

---

## 📦 Paket Utama yang Digunakan

- **langchain** & **langchain-core**
- **langserve[all]** & **sse-starlette**
- **fastapi** & **uvicorn**
- **streamlit**
- **langchain-ollama**
- **langchain-google-genai**
- **python-dotenv**
