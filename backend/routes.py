

from fastapi import APIRouter, HTTPException
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