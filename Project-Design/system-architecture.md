Architecture: 3-Tier
Tier 1 - Frontend: HTML, CSS, JS (Jinja2 Templates) - index.html, result.html
Tier 2 - Backend: FastAPI (main.py) - Handles routing, validation.
Tier 3 - AI & DB: gemini_service.py (Prompt -> Gemini) and database.py (SQLite)

Flow: User Form -> /generate-workout -> Prompt Engineering -> Gemini API -> JSON Parse -> Save to SQLite -> Show Result Page
