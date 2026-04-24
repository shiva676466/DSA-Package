from utils.file_handler import load_json
import requests

API_BASE = "https://dsa-package-api.onrender.com"

def get_quiz(topic):
    """
    Fetch quiz questions from FastAPI backend.
    Falls back to local questions.json if backend is unavailable.
    """
    try:
        response = requests.get(f"{API_BASE}/quiz/{topic}", timeout=3)
        if response.status_code == 200:
            return response.json().get("questions", [])
    except Exception:
        pass

    # fallback to local JSON
    data = load_json("questions.json")
    return data.get(f"{topic}_quiz", [])