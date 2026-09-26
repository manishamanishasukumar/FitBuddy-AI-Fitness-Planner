This folder contains the actual source code.
- frontend/ -> templates/index.html, result.html
- backend/ -> main.py (All FastAPI routes)
- ai/ -> gemini_service.py (Prompt to Gemini)
- database/ -> database.py (SQLite connection)

How to Run:
1. pip install -r requirements.txt
2. Create .env with GOOGLE_API_KEY=your_key
3. uvicorn app.main:app --reload
4. Open http://127.0.0.1:8000 and http://127.0.0.1:8000/docs
