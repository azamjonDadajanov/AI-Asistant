# 🤖 AI Chat Bot

A real-time AI chatbot powered by **Google Gemini API** with a **FastAPI** backend and a vanilla **HTML/CSS/JS** frontend.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![Gemini](https://img.shields.io/badge/Gemini-3.5--flash-orange)

## 📁 Project Structure

```
├── main.py                 # FastAPI backend server
├── .env                    # Environment variables (API key)
├── frontend/
│   ├── index.html          # Chat UI
│   ├── main.css            # Styles
│   └── main.js             # Frontend logic
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd 2-video
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn python-dotenv google-genai
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the server

```bash
python main.py
```

The API server will start at `http://localhost:8000`.

### 5. Open the frontend

Open `frontend/index.html` in your browser.

## 🔌 API Endpoints

| Method | Endpoint     | Description              |
|--------|-------------|--------------------------|
| GET    | `/`         | Welcome message          |
| POST   | `/api/chat` | Send a message to the AI |

### POST `/api/chat` — Request Body

```json
{
  "message": "Hello!",
  "history": [
    { "role": "user", "content": "Hi" },
    { "role": "model", "content": "Hello! How can I help?" }
  ],
  "system_introductins": "You are a helpful assistant."
}
```

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Pydantic
- **AI:** Google Gemini 3.5 Flash (`google-genai`)
- **Frontend:** HTML, CSS, JavaScript
- **Icons:** Font Awesome 7

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

