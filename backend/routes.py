from fastapi import APIRouter, HTTPException
from models import ScoreRequest, ScoreResponse, LoginRequest, LoginResponse, FeedbackRequestfrom datetime import datetime
import json
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_json(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_json(file_name, data):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def append_json_list(file_name, item):
    data = load_json(file_name)
    if not isinstance(data, list):
        data = []
    data.append(item)
    save_json(file_name, data)


@router.get("/")
def home():
    return {"message": "DSA Package API Running 🚀"}


@router.get("/topics")
def get_topics():
    theory = load_json("theory.json")
    return {"topics": list(theory.keys())}


@router.get("/quiz/{topic}")
def get_quiz(topic: str):
    questions = load_json("questions.json")
    key = f"{topic.lower()}_quiz"

    if key not in questions:
        raise HTTPException(status_code=404, detail="Topic quiz not found")

    return {
        "topic": topic,
        "questions": questions[key]
    }


@router.get("/code/{topic}")
def get_code(topic: str):
    code = load_json("code.json")

    if topic.lower() not in code:
        raise HTTPException(status_code=404, detail="Code topic not found")

    return {
        "topic": topic,
        "code": code[topic.lower()]
    }


@router.get("/progress")
def get_progress():
    progress = load_json("progress.json")
    return progress


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    return {
        "message": "Login successful ✅",
        "username": payload.username
    }


@router.post("/score", response_model=ScoreResponse)
def save_score(payload: ScoreRequest):
    percentage = round((payload.score / payload.total) * 100, 2)

    scores = load_json("scores.json")
    if not isinstance(scores, list):
        scores = []

    scores.append({
        "username": payload.username,
        "topic": payload.topic,
        "score": payload.score,
        "total": payload.total,
        "percentage": percentage,
        "timestamp": datetime.now().isoformat()
    })

    save_json("scores.json", scores)

    return {
        "message": "Score saved successfully ✅",
        "username": payload.username,
        "topic": payload.topic,
        "percentage": percentage
    }


@router.get("/leaderboard")
def leaderboard():
    scores = load_json("scores.json")
    if not isinstance(scores, list):
        scores = []

    scores.sort(key=lambda x: x.get("percentage", 0), reverse=True)
    return {"leaderboard": scores[:10]}


@router.post("/feedback")
def feedback(payload: FeedbackRequest):
    append_json_list("feedback.json", {
        "username": payload.username,
        "message": payload.message,
        "rating": payload.rating,
        "timestamp": datetime.now().isoformat()
    })

    return {"message": "Feedback submitted successfully ✅"}