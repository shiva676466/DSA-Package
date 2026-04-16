from utils.file_handler import load_json

def get_theory(topic):
    data = load_json("theory.json")
    return data.get(topic, "No theory found")

def get_questions(topic):
    data = load_json("questions.json")
    return data.get(topic, [])

def get_code(topic, language):
    data = load_json("code.json")
    return data.get(topic, {}).get(language, "Code not found")